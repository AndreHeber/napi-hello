const addon = require('./build/Release/hello');

console.log('Testing native addon...');
const result = addon.hello();
console.log('Result:', result);

// Simple test
if (result === 'Hello, World!') {
  console.log('✅ Test passed!');
  process.exit(0);
} else {
  console.error('❌ Test failed! Expected "Hello, World!" but got:', result);
  process.exit(1);
}