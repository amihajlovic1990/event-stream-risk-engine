# Streaming Semantics

Risk features are evaluated against business event time, not only processing
time. Production state must be bounded by entity, feature window, and retention.

Late events require an explicit policy: recompute, compensate, or ignore after
a watermark. Mixing policies silently creates non-reproducible decisions.
