//this file was generated by ../../../../scripts/onnx_generator/OperatorHeader.py
# ifndef OPERATOR_OPERATOR__ONNX__CONSTANT__12_H
# define OPERATOR_OPERATOR__ONNX__CONSTANT__12_H

# include "operators/operator.h"
# include "operators/operator_stub.h"
# include "operators/operator_info.h"

/**
 * onnx operator 'Constant' version 12
 *
 * @param[in]  ctx  Operator context
 * @return          Status code
 *
 * This operator produces a constant tensor. Exactly one of the provided attributes, either value, sparse_value,
 * or value_* must be specified.
 * 
 * Constraint T:
 *   Constrain input and output types to all tensor types.
 *   Allowed Types: tensor_bool, tensor_complex128, tensor_complex64,
 *                  tensor_double, tensor_float, tensor_float16, tensor_int16,
 *                  tensor_int32, tensor_int64, tensor_int8, tensor_string,
 *                  tensor_uint16, tensor_uint32, tensor_uint64, tensor_uint8

 * Output T output:
 *   Output tensor containing the same value of the provided tensor.
 *   Allowed Types: tensor_bool, tensor_complex128, tensor_complex64,
 *                  tensor_double, tensor_float, tensor_float16, tensor_int16,
 *                  tensor_int32, tensor_int64, tensor_int8, tensor_string,
 *                  tensor_uint16, tensor_uint32, tensor_uint64, tensor_uint8
 * Attribute SPARSE_TENSOR sparse_value :
 *   The value for the elements of the output tensor in sparse format.
 * 
 * Attribute TENSOR value :
 *   The value for the elements of the output tensor.
 * 
 * Attribute FLOAT value_float :
 *   The value for the sole element for the scalar, float32, output tensor.
 * 
 * Attribute FLOATS value_floats :
 *   The values for the elements for the 1D, float32, output tensor.
 * 
 * Attribute INT value_int :
 *   The value for the sole element for the scalar, int64, output tensor.
 * 
 * Attribute INTS value_ints :
 *   The values for the elements for the 1D, int64, output tensor.
 * 
 * Attribute STRING value_string :
 *   The value for the sole element for the scalar, UTF-8 string, output
 *   tensor.
 * 
 * Attribute STRINGS value_strings :
 *   The values for the elements for the 1D, UTF-8 string, output tensor.
 *
 * @since version 12
 *
 * @see io/onnx/onnx/defs/generator/defs.cc:171
 * @see https://github.com/onnx/onnx/blob/master/docs/Operators.md#Constant
 */
extern __attribute__((weak))
operator_status operator__onnx__constant__12(
    node_context *ctx
);

operator_executer resolve_operator__onnx__constant__12(
    node_context *ctx
);

extern __attribute__((weak)) operator_info info_operator__onnx__constant__12;


# endif