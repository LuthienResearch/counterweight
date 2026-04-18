# Plan: Team Section + Blog Link on v10 Landing Page

## Status: Implemented

## PRs
- **PR #2**: [feat: team section with photos, bios, and social links](https://github.com/LuthienResearch/luthien-pbc-site/pull/2) - Draft
- **PR #3**: [feat: blog infrastructure + first post](https://github.com/LuthienResearch/luthien-pbc-site/pull/3) - Draft (needs Scott content review)

## What was done

### PR 1: Team Section
- Added team section between Architecture and CTA on v10 landing page
- Two co-founder cards: Jai Dhyani (Co-Founder & CEO) and Scott Wofford (Co-Founder)
- Circular GitHub avatar photos (120px), names, roles, bios, icon links
- Two-column grid on desktop, stacks to single column on mobile
- Nav link + scroll spy for `#team`
- Expanded footer with GitHub and Contact links

### PR 2: Blog Infrastructure + First Post
- Blog index page at `site/blog/index.html`
- First post: "Why Proxying the API is a Good Basis for a Control System" at `site/blog/why-proxy-openai-api/index.html`
- Source: ControlConf HLD from `luthien-org/luth-gdrive-clone/Scott's folder/why proxying the OpenAI API...`
- Adapted into readable blog format with TL;DR box, comparison table, clean sections
- Blog nav link and footer links added to v10 landing page
- Same dark theme, fonts, responsive design

## Next steps
- Scott reviews blog post content
- Merge PR #2 (team section)
- After PR #2 merges, merge PR #3 (blog) — or rebase if needed
- Future: migrate blog to Substack (supports backdating)
