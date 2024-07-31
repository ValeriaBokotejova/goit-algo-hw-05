## Results

| Test Case                |   Boyer-Moore (s) |   KMP (s) |   Rabin-Karp (s) |
|:-------------------------|------------------:|----------:|-----------------:|
| Article 1 - existing     |          0.001974 |  0.007588 |         0.00976  |
| Article 2 - existing     |          0.025833 |  0.092387 |         0.126951 |
| Article 1 - non_existing |          0.05203  |  0.381546 |         0.553285 |
| Article 2 - non_existing |          0.082117 |  0.566716 |         0.797253 |

## Conclusions

The Boyer-Moore algorithm was the fastest in both articles for both existing and non-existing substrings. It was much faster than the other algorithms, especially when searching for non-existing substrings.
