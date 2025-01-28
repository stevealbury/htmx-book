```rust
+--------------------------------+-------------------------------------------------------------------+----------------------------------------------+
| String Type                    | Description & Use                                                  | Code Example                                  |
+--------------------------------+-------------------------------------------------------------------+----------------------------------------------+
| &str (string slice)           | - An immutable reference to a UTF-8 string slice.                   | fn main() {                                   |
|                                | - Often references a string literal or part of another string.     |     let greeting: &str = "Hello, world!";    |
|                                | - Does not own the data (borrowed).                                |     println!("{}", greeting);                |
|                                |                                                                     | }                                            |
+--------------------------------+-------------------------------------------------------------------+----------------------------------------------+
| String (owned)                | - A growable, mutable, UTF-8 string stored on the heap.             | fn main() {                                   |
|                                | - Owns its contents and can be modified.                           |     let mut greeting = String::from("Hello");|
|                                | - Useful when you need to build or store strings over time.        |     greeting.push_str(", world!");           |
|                                |                                                                     |     println!("{}", greeting);                |
|                                |                                                                     | }                                            |
+--------------------------------+-------------------------------------------------------------------+----------------------------------------------+
| Cow<str> (clone-on-write)     | - Represents either a borrowed `&str` or an owned `String`.         | use std::borrow::Cow;                        |
|                                | - Avoids allocations unless mutation is required.                  |                                             |
|                                | - Helpful in APIs to handle both borrowed/owned cases elegantly.   | fn greet(name: &str) -> Cow<str> {           |
|                                |                                                                     |     if name == "world" {                     |
|                                |                                                                     |         "Hello, world!".into()               |
|                                |                                                                     |     } else {                                 |
|                                |                                                                     |         let mut s = String::from("Hello, "); |
|                                |                                                                     |         s.push_str(name);                    |
|                                |                                                                     |         s.into()                              |
|                                |                                                                     |     }                                        |
|                                |                                                                     | }                                            |
|                                |                                                                     | fn main() {                                   |
|                                |                                                                     |     println!("{}", greet("world"));          |
|                                |                                                                     |     println!("{}", greet("Rust"));           |
|                                |                                                                     | }                                            |
+--------------------------------+-------------------------------------------------------------------+----------------------------------------------+
| OsString                       | - Used for platform-specific, possibly non-UTF-8 strings.           | use std::ffi::OsString;                      |
|                                | - Commonly for file paths or environment variables.                |                                              |
|                                | - Owned and mutable; handles OS encodings safely.                   | fn main() {                                   |
|                                |                                                                     |     let mut command = OsString::from("ls");  |
|                                |                                                                     |     command.push(" -la");                    |
|                                |                                                                     |     println!("{:?}", command);               |
|                                |                                                                     | }                                            |
+--------------------------------+-------------------------------------------------------------------+----------------------------------------------+
| CString (C-compatible)         | - A null-terminated C-compatible string.                            | use std::ffi::CString;                       |
|                                | - Must not contain interior null bytes.                            |                                              |
|                                | - Useful for interoperability with C (FFI).                        | fn main() {                                   |
|                                |                                                                     |     let c_string = CString::new("Hello!")    |
|                                |                                                                     |         .expect("Failed to create CString"); |
|                                |                                                                     |     // c_string.as_ptr() can be used in C    |
|                                |                                                                     |     println!("{:?}", c_string);             |
|                                |                                                                     | }                                            |
+--------------------------------+-------------------------------------------------------------------+----------------------------------------------+

```
