{
  "targets": [{
    "target_name": "hello",
    "cflags!": [ "-fno-exceptions" ],
    "cflags_cc!": [ "-fno-exceptions" ],
    "sources": [ "hello.cc" ],
    "include_dirs": [
      "<!@(node -p \"require('node-addon-api').include\")"
    ],
    "defines": [ "NAPI_DISABLE_CPP_EXCEPTIONS" ],
    'conditions': [
      ['OS=="win"', {
        "defines": [
          "_HAS_EXCEPTIONS=1"
        ],
        "msvs_settings": {
          "VCCLCompilerTool": {
            "ExceptionHandling": 1
          }
        }
      }]
    ]
  }]
} 