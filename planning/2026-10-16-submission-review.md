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

1. Updated per the candidate's supplied order: the recommendation form remains
   blank for annual review and is completed at final tenure/promotion. The annual
   status worksheet is represented by its link in Employment History.
2. Confirm whether Tara also needs to sign the consultation acknowledgment on
   evaluation page 14. Both signatures already appear on the ratings page 5.
3. Confirm that the retained position description covers both review years.
4. Reordered the packet: directed, non-directed and RSCAD evidence follows each
   relevant summary; position description and 2025/2026 evaluations follow RSCAD;
   the previous supervisor letter follows evaluations and precedes the Vita.
   The chronology and source notes/index follow the Vita as supporting material.
5. The newly supplied `2026.02_molik_tenure_letter_signed.pdf` is byte-identical
   to retained P1.3 (`evidence/2025/reappointment-letter-signed.pdf`), SHA-256
   `36af4e3b37635758bb639f714e40201a17dfe5c4849d4b560228d8f7046c3314`.
   It is Tara Coleman's February 10, 2026 recommendation with committee feedback,
   not a Dean's congratulatory letter. All four pages remain included.

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
tests skipped. The earlier evaluation-addition build had 532 pages; page locations have changed
following the document-order correction.
The retained evaluation hash matches the supplied original. Existing font and
underfull-box warnings remain. The documented temporary ARM Biber workaround
was required for the installed macOS universal binary.

The signed original is retained separately from `evidence/2026/evaluation_2026_packet_display.pdf`.
The latter is generated using `qpdf --flatten-annotations=all` to preserve the
visible digital signature during LaTeX inclusion. It is a display derivative,
not a cryptographically signed original; its hash is recorded in the manifest.

## Document-order verification

Pulled main through `9290d6d` before editing. The reordered 537-page packet places
P1.3 on PDF pages 520–523, immediately before the Vita on page 524. All four
letter pages and the source signatures were visually checked. The blank
recommendation page transcribes the retained form fields without the obsolete
Year 1 / January 2025 header. ModernCV footer width now accommodates the full
packet page count. All retained source PDF hashes remain unchanged.
