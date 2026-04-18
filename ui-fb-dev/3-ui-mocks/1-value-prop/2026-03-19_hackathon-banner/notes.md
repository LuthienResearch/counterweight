# Hackathon Banner Mocks (v10.9)

**Date:** 2026-03-19
**Purpose:** Add a prominent banner to the PBC landing page promoting Jai's talk at the AI Control Hackathon 2026.

## Event Details

- **Event:** AI Control Hackathon 2026
- **Organizers:** Apart Research x Redwood Research
- **Dates:** March 20-22, 2026
- **Jai's Talk:** "Luthien Proxy: Real-World AI Control"
  - Friday March 20, 12:00-12:45 PM PDT
  - Zoom
- **Attendees:** 655+
- **Registration:** https://luma.com/ai-control-hackathon-2026-jai-dhyani?tk=bfMBjG
- **Hackathon page:** https://apartresearch.com/sprints/ai-control-hackathon-2026-03-20-to-2026-03-22
- **Project ideas (ours):** `site/hackathon/index.html` in luthien-pbc-site

## Apart Research Branding

- Neon green accent: `#46ff99`
- Their site uses dark backgrounds with green accents
- Co-organized with Redwood Research

## Design Rationale

The existing v10.8 has a hackathon section buried at the bottom of the page. With the event happening tomorrow, we need a high-visibility banner near the top. Four options explored:

- **Option A:** Full-width strip below nav. Minimal, one line, dismiss button. Uses Luthien blue (`#6b9fff`).
- **Option B:** Card-style section after hero. More room for details. Reuses existing `.section` pattern.
- **Option C:** Same as Option A but with Apart's neon green (`#46ff99`). Signals "partner event."
- **Option D:** Jai's hero banner from PR #15. Bold, theatrical, scanline texture + blue glows. Already coded.

## Files

- `option-a.html` - Full-width strip (Luthien blue accent)
- `option-b.html` - Card section after hero
- `option-c.html` - Full-width strip (Apart green accent)
- `option-d.html` - Hero banner from PR #15 (adapted)
