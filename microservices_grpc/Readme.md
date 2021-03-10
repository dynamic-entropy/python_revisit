`python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. recommendpb/recommend.proto`

. python3 -m grpc_tools.protoc runs the compiler that generates python code
. -I --> tell the compiler where to find the files
. --python_out --grpc_python_out --> where to output the compiled files
. path to protobuf file relative to I
