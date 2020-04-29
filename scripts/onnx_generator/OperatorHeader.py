import os
import inspect
import pathlib

class OperatorHeader:
    _template_header = '''
//this file was generated by {script}
# ifndef OPERATOR_{header_name}_H
# define OPERATOR_{header_name}_H

# include "operators/operator.h"
# include "operators/operator_stub.h"

{doxygen}
{prototype}

operator_executer resolve_{operator_name}(
  size_t                  n_input,
  Onnx__TensorProto    ** input,
  size_t                  n_attribute,
  Onnx__AttributeProto ** attribute,
  size_t                  n_output,
  Onnx__TensorProto    ** output
);

{aliases}
# endif
'''
    _template_doxygen = '''
/**
 * {domain} operator '{name}' version {version}
 *
 * @param[in]  n_input     Number of inputs ({range_input})
 * @param[in]  input       Array of pointers to the inputs
 * @param[in]  n_attribute Number of attributes
 * @param[in]  attribute   Array of pointers to the attributes
 * @param[in]  n_output    Numper of outputs ({range_output})
 * @param[out] output      Array of pointer to the outputs
 * @return                 Error code
 *
 * @retval     0        No Error
 * @retval     ENOSYS   Operator is stubbed
 * @retval     EINVAL   Invalid argument
 * @retval     ENOMEM   Out of Memory
 * @retval     EFAULT   Invalid addr
 * @retval     EDOM     Math argument out of domain
 * @retval     ERANGE   Math result not representable
 *
{doc}
{deprecated}
{constraints}
{inputs}
{outputs}
{attributes}
 *
 * @since version {version}
 *
{defs_filepath}
{doc_ref}
 */
'''
    _template_prototype = '''
{attribute}
operator_status {operator_name}(
  size_t                  n_input,
  Onnx__TensorProto    ** input,
  size_t                  n_attribute,
  Onnx__AttributeProto ** attribute,
  size_t                  n_output,
  Onnx__TensorProto    ** output
);
'''

    def __init__(self, schema, path):
      self.schema = schema
      self.path = path

    def text(self):
        doxygen = self._template_doxygen.format(
            attributes=self.schema.attributes.text(" * "),
            deprecated=" * " + "@deprecated Avoid usage!" * self.schema.deprecated,
            doc=self.schema.doc.text(" * "),
            doc_ref=" * @see " + self.schema.ref_doc,
            domain=self.schema.domain,
            constraints=self.schema.constraints.text(" * "),
            range_input=self._range(*self.schema.range_input),
            inputs=self.schema.inputs.text(" * "),
            name=self.schema.name,
            range_output=self._range(*self.schema.range_output),
            outputs=self.schema.outputs.text(" * "),
            version=self.schema.version,
            defs_filepath=f" * @see {self._rel_path(self.schema.ref_file[0])}:{self.schema.ref_file[1]}",
        ).strip()
        prototype = self._template_prototype.format(
            attribute="__attribute__((deprecated))\n" if self.schema.deprecated else "" ,
            operator_name = self.schema.operator_name,
        ).strip()
        aliases = "".join([
            self._template_prototype.format(
                # attribute=f'extern __attribute__((weak{", deprecated" if self.schema.deprecated else ""}))',
                attribute=f'extern __attribute__((weak))',
                operator_name = f"{self.schema.operator_name}__{t}"
            )
            for t in self.schema.constraints.typePermutations()
        ])
        return self._template_header.format(
            script=self._rel_path(inspect.getfile(inspect.currentframe())),
            header_name=self.schema.operator_name.upper(),
            operator_name=self.schema.operator_name,
            doxygen = doxygen,
            prototype = prototype,
            aliases = aliases,
        )

    def filename(self, path=None):
        path = str(self.path) if path == None else str(path)
        path += f"/{self.schema.domain}"
        path += f"/{self.schema.operator_name}.h"
        return pathlib.Path(path)

    def __str__(self):
        return self.text()

    def _range(self, min, max):
      if (min == max):
          return f"always {min}"
      else:
          return f"{min} to {max}"

    def _rel_path(self, path):
        return os.path.relpath(os.path.realpath(path),os.path.realpath(self.path))

    def __repr__(self):
        return f"OperatorHeader({self.schema.__repr__()}, {self.path.__repr__()})"