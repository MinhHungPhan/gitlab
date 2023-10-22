# Understanding YAML

## Table of Contents

- [Introduction](#introduction)
- [What is YAML?](#what-is-yaml)
- [Understanding Key-Value Pairs](#understanding-key-value-pairs)
- [Working with Lists and Arrays](#working-with-lists-and-arrays)
- [Understanding Indentation](#understanding-indentation)
- [Comments in YAML](#comments-in-yaml)
- [YAML vs JSON](#yaml-vs-json)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Welcome to this guide designed to provide you with a fundamental understanding of YAML. Until now, you might have encountered YAML but didn't delve deep into its structure. This section aims to change that, giving you enough information to write effective configuration files and leverage the language's powerful features.

## What is YAML?

YAML, at its core, is a straightforward way to represent data structures. In simpler terms, it is a human-readable data serialization format. If you've been writing YAML files or defining pipelines in GitLab CI, it's time to go back to the basics and truly understand YAML.

## Understanding Key-Value Pairs

The primary structure in YAML is the key-value pair. For instance:

```yaml
name: John
```

Here, `name` acts as the key, and `John` is its corresponding value. YAML supports various data types such as strings, integers, and booleans. Another example:

```yaml
age: 29
isMale: true
```

## Working with Lists and Arrays

YAML offers the flexibility to create lists or arrays containing multiple items:

```yaml
stuff:
  - laptop
  - car
  - bike
```

Alternatively, you can also use square brackets to denote a list:

```yaml
food: [pizza, donuts, coke]
```

## Understanding Indentation

Indentation is crucial in YAML as it represents the structure and hierarchy of the data. By nesting properties under a specific key, they become children of that key. For instance:

```yaml
person:
  name: John
  age: 29
  isMale: true
  stuff:
    - laptop
    - car
    - bike
```

> Note that `name`, `age`, `isMale`, and `stuff` are all properties of the `person` object.

## Comments in YAML

Comments can be included in a YAML file using the `#` symbol. For example:

```yaml
# This is a comment
```

This capability is an advantage over JSON, which does not support comments.

## YAML vs JSON

YAML and JSON are quite similar, but YAML is generally considered more human-readable. You can even convert YAML into JSON and vice versa. Many online converters can help you visualize this transformation, offering clarity on the structure.

```json
{
  "person": {
    "name": "John",
    "age": 29,
    "isMale": true,
    "stuff": ["laptop", "car", "bike"]
  }
}
```

If you're already familiar with JSON, transitioning to YAML will likely feel more streamlined due to the reduced need for quotes and brackets.

## Conclusion

YAML, with its human-readable format and flexible structure, is an invaluable tool for defining configuration files, writing data serialization, and much more. As with any language, practice is key. The more you work with YAML, the more intuitive it becomes. Whether you're a seasoned JSON veteran or a complete beginner, YAML offers a concise and efficient way to represent data.

## References

- [Online YAML to JSON Converter](https://codebeautify.org/yaml-beautifier)

*Happy Coding!* 🚀