---
layout: page
section: Tools
title: Converters
order: 900
javascript_components:
  - converters.js
---

* TOC
{:toc}

# Measurement

## Inch

The inch (symbol: `in` or `″`) is a unit of length in the British imperial and the United States customary systems of measurement.
`1` inch is `2.54` centimeters.

<div id="#converter-inch"></div><script>render("#converter-inch", "inch")</script>

## Foot

The foot (plural - feet, symbol: `ft` or `'`) is a unit of length in the British imperial and the United States customary systems of measurement.
`1` foot is `30.48` centimeters.

<div id="#converter-foot"></div><script>render("#converter-foot", "foot")</script>

## Mile

The mile (symbol: `mi`) is a unit of distance in the British imperial and the United States customary systems of measurement.
`1` mile is `1.61` kilometers.

<div id="#converter-mile"></div><script>render("#converter-mile", "mile")</script>

## Pound

The pound or pound-mass (symbol: `lb`) is a unit of mass in the British imperial and the United States customary systems of measurement.
`1` pound is `0.45359237` kilograms.

<div id="#converter-pound"></div><script>render("#converter-pound", "pound")</script>

## Ounce

The ounce or ounce-mass (symbol: `oz`) is a unit of mass in the British imperial and the United States customary systems of measurement.
`1` ounce is `28.349523125` grams (`1/16` of pound).

<div id="#converter-ounce"></div><script>render("#converter-ounce", "ounce")</script>

## Gallon

The gallon (symbol: `US gal`, `US dry gal`, `imp gal`) is a unit of volume in the British imperial and the United States customary systems of measurement.
`1` US gallon is `3.785411784` litres, `1` US dry gallon is `4.40488377086` litres, `1` imperial gallon is `4.54609` litres.

<div id="#converter-gallon-us"></div><script>render("#converter-gallon-us", "gallon_us")</script>
<div id="#converter-gallon-us-dry"></div><script>render("#converter-gallon-us-dry", "gallon_us_dry")</script>
<div id="#converter-gallon-imperial"></div><script>render("#converter-gallon-imperial", "gallon_imperial")</script>

# Network

## CIDR

Classless Inter-Domain Routing (CIDR) is a method for allocating IP addresses and IP routing.
Number after `/` represents the number of network bits (unchanged and always `1`) in the IP address.
The objective of CIDR it to improve the previous classful network addressing architecture
(3 classes - Class A: `/8`, Class B: `/16`, Class C: `/24`).

<div id="#converter-cidr"></div><script>render("#converter-cidr", "cidr")</script>

# Encoding

## Base64

Base64 is an encoding algorithm that transform any characters (binary data) into an alphabet which consists `64` symbols:
uppercase and lowercase Roman letters (`A–Z`, `a–z`), numerals (`0–9`), `+` and `/` symbols.
The `=` symbol is also used as a padding suffix (can be optional).

<div id="#converter-base64"></div><script>render('#converter-base64', 'base64')</script>

# Cryptographic

## MD5

The `MD5` (Message Digest 5) is a cryptographic hash function which produces a `128-bit` hash value.
It has been cryptographically broken and considered **insecure** (it should not be used).

<div id="#converter-md5"></div><script>render('#converter-md5', 'md5')</script>

## SHA1

The `SHA-1` (Secure Hash Algorithm 1) is a cryptographic hash function which produces a `160-bit` hash value.
It has been cryptographically broken and considered **insecure** (it should not be used).

<div id="#sha1"></div><script>render('#sha1', 'sha1')</script>

## SHA2

The `SHA-2` (Secure Hash Algorithm 2) is a set of cryptographic hash functions, it consists hash functions
which produce `224-bit`, `256-bit`, `384-bit` or `512-bit` hash values.

<div id="#sha224"></div><script>render('#sha224', 'sha224')</script>
<div id="#sha256"></div><script>render('#sha256', 'sha256')</script>
<div id="#sha384"></div><script>render('#sha384', 'sha384')</script>
<div id="#sha512"></div><script>render('#sha512', 'sha512')</script>

# Other

## htpasswd

The `htpasswd` is used to store usernames and passwords for basic HTTP authentication (used in `Apache` and `nginx`). It supports different formats for password:

- `bcrypt`: `$2y$` or `$2a$` + the result of the `crypt_blowfish` algorithm. **Secure.**
- `MD5`: `$apr1$` + the result of the `Apache-specific MD5 algorithm`. Common but insecure.
- `SHA1`: `{SHA}` + Base64-encoded SHA-1. Insecure.
- `CRYPT`: Unix `crypt` function with a randomly-generated 32-bit salt. Insecure.
- `PLAIN TEXT`: Unencrypted. Insecure.

<div id="#converter-htpasswd"></div><script>render('#converter-htpasswd', "htpasswd")</script>
