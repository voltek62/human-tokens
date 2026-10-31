# How many tokens of thought per second?

*Version française : [README.fr.md](README.fr.md)*

A single-page, serverless test to measure your own throughput in "tokens of thought" and compare it with the **150 tokens per second** that Saturnin Pugnet attributes to every human, with published scientific measurements, and with the output speed of large language models.

**Take the test:** https://voltek62.github.io/human-tokens/

Everything runs in the browser. Nothing is recorded or transmitted. Interface and content in **English, French and Spanish**. The browser language is used by default; `#en`, `#fr` or `#es` in the address forces a language for a shared link, and the switcher at the top of the page remembers your choice.

## Why

On the Silicon Carne podcast of 28 October 2026 (at 32:49), Saturnin Pugnet, a founding member of World with Sam Altman, states that "roughly, every person thinks at 150 tokens of thought per second". From there he concludes that by 2036 AI will produce, every year, as many tokens of thought as all of humanity since the beginning of time.

That figure is a working assumption, not a measurement. His manifesto *Phase Lock* does not contain it, and his own totals work out closer to 2 tokens per second per person. The full source file is in [SOURCES.md](SOURCES.md) (in French).

Rather than argue about the right number, this project gives everyone a way to measure their own.

## The four tests

| Test | What it measures | Published reference |
|---|---|---|
| Silent reading | Text input rate. One text drawn at random from four (the dance of the bees, Morse code, measuring the metre, the Antikythera mechanism), with two comprehension questions. | 238 words/min (Brysbaert 2019) |
| Reading aloud | Speech rate | 150 to 183 words/min |
| Typing | Output rate at the keyboard | 52 words/min (Dhakal et al. 2018) |
| Reasoning | Four problems drawn from a bank of forty-five (everyday arithmetic, plus five of medium difficulty), answers verified by computation. For each problem you solve, we count the tokens of the written reasoning a model would produce, divided by your time. Wrong answers do not count. | 10 bits/s (Zheng & Meister 2025) |

Passages are counted with the o200k tokenizer (GPT-4o and later) via [gpt-tokenizer](https://github.com/niieani/gpt-tokenizer) when it loads, otherwise with a per-character estimate. References in words per minute are converted with the tokens-per-word ratio of the selected language: 1.2 for English, 1.35 for Spanish, 1.5 for French (measured on o200k).

The dashboard gives a qualitative reading (median, strength, bottleneck, gap with a model at 100 tok/s) and three ready-to-copy share texts: LinkedIn, X / Bluesky / Threads, and a one-liner.

## Structure

```
src/head.html   title, fonts, tokenizer loading
src/page.html   styles, content, script: reading texts, problem bank, three-language interface
build.py        assembles index.html
index.html      the complete page, served by GitHub Pages
SOURCES.md      source file, calculations, problem answers (French)
```

Edit `src/`, then:

```sh
python3 build.py
```

## Contributing

Ideas welcome: more languages (add an entry to `LANGS`, `UI`, `READ`, `SPEAK`, `TYPE` and to each problem), a listening test, more texts or problems, a better calibration of the reasoning test. Open an issue or a pull request.

## Licence

MIT. The reading passages are original and under the same licence.
