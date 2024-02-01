# Big Endian Obfuscator 💻

### Description ℹ️:
 An implementation of the "Big Endian Obfuscation" Algorithm, a javascript obfuscation algorithm which was discovered in the wild being used by threat actors in credential phishing campaigns to effectively evade anti-phishing bots and crawlers' detection.
 Used to obfuscate phishing page source code.
 
### Snippet of obuscated HTML code 📃:

![Obfuscated source](https://i.imgur.com/ePHL00v.png)

### Steps taken to replicate 📝:

- [X] Reverse engineered JS code
- [X] Replicated algorithm
- [X] Optimized algorithm to reduce file output size (array literals)
- [X] Implemented JS code auto-generation in python

### Usage ⚙️:

```
python bigendian.py
```

### Phish detection and tracking ⚠️:

- [Google Transparency Report](https://transparencyreport.google.com/safe-browsing/search)
- [PhishTank](https://www.phishtank.com)
- [VirusTotal](https://www.virustotal.com)
- [URLScan.io](https://urlscan.io)
- [Norton Safe Web](https://safeweb.norton.com)
- [APWG](https://antiphishing.org/reportphishing/)
  


### Description of Big and Little Endianness ℹ️: 

[Endianness](https://en.wikipedia.org/wiki/Endianness) is simply the order in which a sequence of bytes is stored in computer memory.


### Endianness is primarily expressed as:

- Big-endian (BE) 📉
- Little-endian (LE) 📈.


> In the Big endian system the most significant byte (the big end) in a sequence ([word](https://en.wikipedia.org/wiki/Word_(computer_architecture))) is stored first at the lowest/smallest memory address and the least significant byte at the largest.

> In contrast, in the Little endian system the least significant byte is stored first at the lowest/smallest memory address and the most significant byte at the largest.


### Fun fact 😁:

> The usage of the terms big endian and little endian were [inspired by](https://www.ling.upenn.edu/courses/Spring_2003/ling538/Lecnotes/ADfn1.htm) a passage in *Gulliver's Travels (1726)* in which the author used them to describe the two oppositions in a dispute on whether to crack a boiled egg by its big end or its little end.
