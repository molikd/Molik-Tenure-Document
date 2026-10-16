# October 16, 2026 submission review

## Evaluation added

Retained the candidate-supplied `2026-self-evaluation-Molik.pdf` byte-identical as
`evidence/2026/evaluation_signed_2026.pdf` (24 pages), registered as P1.4 and
included in the packet alongside the signed 2025 evaluation. Source page 5 has
both signatures and an overall Exceeds Expectations rating. Source page 14 has
the employee signature, but the supervisor acknowledgment line is blank. Do not
edit the signed PDF to correct text or add signatures; obtain a replacement
through the original signing workflow if needed.

## Requirement checked

The publicly posted Libraries department document, Part I, portfolio list
item 10(h), printed page 14 (PDF page 14), calls for “Position descriptions and
evaluations for all years of employment at K-State Libraries.” Item (i) calls
for previous supervisor reappointment recommendation letters. Retain 2025 and
2026. This is the published 2023 document; any later internal procedures should
be checked for superseding details.

Source: https://www.k-state.edu/provost/policies-resources/evaluation-promotion-tenure/department-documents/lib/documents/librariesdeptdocs-2023.pdf

## Submission priorities

1. Resolve the missing current-year recommendation/transmittal form and official
   Annual Status Review Worksheet with HR. The compiled packet still contains an
   explicit pending-form page and a Working Draft cover; do not treat it as a
   finished submission until the disposition of these forms is known.
2. Confirm whether Tara also needs to sign the consultation acknowledgment on
   evaluation page 14. Both signatures already appear on the ratings page 5.
3. Confirm that the retained position description is current and whether a
   separate supervisor workload statement is required for this annual review.
4. Check current instructions for document placement: the published list places
   position descriptions, evaluations and prior recommendation letters before
   the CV. The existing repository assembly puts these in the supplementary
   material after the CV; this review did not silently restructure the packet.

## Optional evaluation polish if a replacement is being issued

- Page 17: “simultainously” should be “simultaneously”; better, omit that word.
- Page 17: omit “with clear reasonable timelines,” which repeats the preceding
  reference to timelines and dependencies.
- Page 7: the sentence beginning “Additionally, ongoing work” could read:
  “Ongoing work on the NSF IUSE effort and follow-up conversations about Gwen
  Sibley’s Purdue University site visit have continued to develop these connections.”
- Page 16 is blank apart from the template header/footer; the response continues
  on page 17. Tighten the pagination in the editable source if reissuing it.

These small editorial issues do not justify altering an already signed original.
The supervisor's wording is preserved as supplied.

## Validation

Both portfolio and CV builds succeeded. Static checks passed with the existing
dateless software bibliography warning; 11 unit tests passed with 3 opt-in
tests skipped. The rebuilt portfolio has 532 pages; P1.4 starts on PDF page 62.
The retained evaluation hash matches the supplied original. Existing font and
underfull-box warnings remain. The documented temporary ARM Biber workaround
was required for the installed macOS universal binary.

The signed original is retained separately from `evidence/2026/evaluation_2026_packet_display.pdf`.
The latter is generated using `qpdf --flatten-annotations=all` to preserve the
visible digital signature during LaTeX inclusion. It is a display derivative,
not a cryptographically signed original; its hash is recorded in the manifest.
