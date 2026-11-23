# A negative answer to mathex's cutoff-series question beyond Ghafari's masks

Haobo Ma (ChronoAI Pte Ltd, Singapore), then Wenlin Zhang (National University of Singapore; ChronoAI Pte Ltd, Singapore). 19 November 2026. CC BY 4.0.

## Result

For the Euclidean five-dimensional series in [mathex's question](https://mathoverflow.net/questions/511715/bound-of-series), revision 2 (26 May 2026), final displayed inequality, a fixed symmetric mask for each nonzero output makes the zero-output value vanish and forces logarithmic divergence at every positive time. This holds for every fixed normalized real or complex compact cutoff continuous at zero. It excludes every finite real constant/exponent pair even when both positive scales lie in an arbitrary interval `(0,E]`. A uniform Lipschitz estimate holds when time is bounded and scales have a positive lower bound; retaining the zero modes gives a linear-in-time obstruction if that time restriction is dropped.

Joe Ghafari's [September 2026 thesis](https://arxiv.org/abs/2609.02197v1), Appendix H, Lemma H.0.1, pp. 108–111, proves a related output-difference bound for a prescribed Littlewood–Paley mask. Its proof uses frequency derivative control, not just support comparability. Corollary 4 shows that the masks above cannot satisfy that control. Ghafari's bound is credited as a prior structured-mask result, not as a proof of the different cutoff-increment estimate.

## Files and rebuilding

- `note.tex` is the only main LaTeX source; the bibliography is embedded. No other scientific inputs are needed.
- `metadata.json` identifies the note, creators, source and mathematical coverage.
- `verify.py` uses Python 3.10 or later and only the standard library. `verification.txt` contains its exact expected output.

Build with Tectonic 0.17.0:

```sh
tectonic note.tex
python3 verify.py > actual-verification.txt
diff -u verification.txt actual-verification.txt
```

Alternatively, use `pdflatex note.tex` twice. No BibTeX pass is necessary because the bibliography is embedded; a BibTeX-based adaptation can use the same two reference entries.

## Mathematical coverage

The proof retains the full square time integral, all Fourier frequency factors, both cutoff squares and every ordered lattice pair, including zero modes. It adopts Euclidean vector norms and real or complex scalar cutoffs. The posing text does not specify those conventions. No extra mask symmetry, partition identity or cutoff monotonicity is assumed.

The pinned [Lean source](https://github.com/the-omega-institute/trureturing/blob/1ad50310295853e27713693f182e8eac94296739/D5/S3/Fourier/MO511715Source.lean) contains `cutoff_finite_support`, `time_integral_ge`, `kernel_block_lower`, `phi_dyadic_growth`, and `result` in namespace `D5.S3.Fourier.MO511715Source`. `cutoff_finite_support` covers every positive scale. The time and block bounds use time one; the block bound and dyadic growth use output `(1,0,0,0,0)` and its selected mask. `phi_dyadic_growth` covers the dyadic sequence and real or complex cutoffs. `result` negates the conjunction of the real and complex universal smooth-cutoff estimates through a real bump. The intermediate private lemma `source_estimate_failure` handles each fixed normalized compact cutoff continuous at zero and every finite real constant and exponent, with time one, first-unit output and larger scale two.

The full all-scale floor bound at arbitrary positive time and nonzero output (Theorem 1), the bounded-interval and symmetric-mask obstruction (Corollary 3), the frequency-derivative obstruction (Corollary 4), the Lipschitz correction (Proposition 5), and the zero-mode time obstruction (Corollary 6) have complete written proofs. The finite checker covers explicit lattice instances, generalized output vectors, mask symmetry, dyadic disjointness, and rational time-region and constant identities. It does not establish the infinite statements or numerically integrate the kernel.

## References and attribution

The posing source is mathex, *Bound of series*, MathOverflow question 511715, revision 2, 26 May 2026 (source text CC BY-SA 4.0). The related positive result is Joe Ghafari, *Paracontrolled approach to the stochastic Cahn–Hilliard equation*, University of Ottawa Ph.D. thesis, arXiv:2609.02197v1, 2 September 2026, Appendix H. The remaining reference is the pinned `.lean` file above. All mathematical arguments needed to read the note appear in `note.tex`; no priority claim is made.
