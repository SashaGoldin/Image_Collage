{ pkgs }: {
  deps = [
    pkgs.xsimd
    pkgs.pkg-config
    pkgs.libxcrypt
    pkgs.cope
    pkgs.python-launcher
    pkgs.pkg
    pkgs.python310Packages.opencv4
    pkgs.python310Packages.tgcrypto
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.xsimd
      pkgs.libxcrypt
      pkgs.libGL
      pkgs.stdenv.cc.cc.lib
    ];
    LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.libGL
      pkgs.stdenv.cc.cc.lib
    ];
  };
}