# Node.js Native Extension - Hello World

This project demonstrates how to create a simple native addon for Node.js using N-API (Node-API). The addon provides a simple "hello world" function that can be called from JavaScript.

## Prerequisites

- Node.js (v14.x or later recommended)
- node-gyp (install globally with `npm install -g node-gyp`)
- C++ build tools:
  - **Windows**: Visual Studio Build Tools
  - **macOS**: Xcode Command Line Tools (`xcode-select --install`)
  - **Linux**: GCC and development tools (`build-essential` package)

## Project Structure

```
.
├── binding.gyp           # Build configuration file
├── hello.cc             # C++ source code
├── package.json         # Node.js package configuration
└── test.js             # Test file to verify the addon
```

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd hello
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Build the native addon:
   ```bash
   npm run build
   ```

## Usage

After building the addon, you can use it in your Node.js code like this:

```javascript
const addon = require('./build/Release/hello');

// Call the hello function
console.log(addon.hello()); // Output: "Hello, World!"
```

## Development

### Building

The project uses `node-gyp` for building the native addon. The build configuration is specified in `binding.gyp`.

To rebuild the project:

```bash
npm run build
```

### Testing

To run the test:

```bash
npm test
```

## API Reference

### hello()

Returns a greeting string.

**Returns**: `string` - Returns "Hello, World!"

## License

MIT

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting

If you encounter build issues:

1. Make sure you have all prerequisites installed
2. Try deleting the `build` directory and rebuilding
3. Update `node-gyp`: `npm install -g node-gyp`
4. Check that your Node.js version is compatible

## Resources

- [Node-API Documentation](https://nodejs.org/api/n-api.html)
- [node-gyp Documentation](https://github.com/nodejs/node-gyp)
- [Node.js Addons Guide](https://nodejs.org/api/addons.html) 