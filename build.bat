@echo off
REM build.bat for Windows

REM Ensure we're in the script's directory
cd /d %~dp0

REM Clone submodule
git submodule init
git submodule update

REM Create temp build dir
rmdir /s /q tempbuild
mkdir tempbuild
cd tempbuild

REM Run CMake configuration
cmake -G "MinGW Makefiles" -DBUILD_DIVSUFSORT64=ON -DBUILD_EXAMPLES=OFF -DUSE_OPENMP=ON -DCMAKE_POLICY_VERSION_MINIMUM=3.5 ..\libdivsufsort

REM Build
cmake --build . --config Release

cd ..

REM Find two largest files and move to pydivsufsort
REM (There’s no direct ‘du -s | sort’ in cmd, so do it statically for now)
copy tempbuild\examples\libdivsufsort64.dll pydivsufsort\
copy tempbuild\examples\libdivsufsort.dll pydivsufsort\

REM Clean up
rmdir /s /q tempbuild
