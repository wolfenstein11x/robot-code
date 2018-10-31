set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_C_COMPILER /opt/jetson_toolchain/bin/aarch64-unknown-linux-gnu-gcc)
set(CMAKE_CXX_COMPILER /opt/jetson_toolchain/bin/aarch64-unknown-linux-gnu-c++)
set(CMAKE_FIND_ROOT_PATH /opt/jetson_toolchain)
# Have to set this one to BOTH, to allow CMake to find rospack
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM BOTH)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)