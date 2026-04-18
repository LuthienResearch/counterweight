# Plan: Build EAG SF Follow-Up Contact List

## Context
Scott attended EAG SF (Feb 13-15, 2026) and met ~35 people across 3 days. Data is scattered across Swapcard screenshots, Google Calendar, Otter.ai transcripts, and handwritten/typed notes in Google Drive. Need to consolidate into a single contact list with matched notes, key takeaways, action items, and priority flags — then save to markdown and update the People Database Google Sheet.

## Data Sources Discovered

| Source | What's There | Count |
|--------|-------------|-------|
| Swapcard screenshots (5 images provided) | Names, titles, orgs, time slots | 34 contacts |
| Google Calendar (Feb 13-15) | Same meetings + extras (Katherine Biewer, Julie Steele, Cameron Berg, Govind, Anish Mohammed) | ~40 events |
| Otter.ai transcripts | Audio recordings from meetings | 21 transcripts |
| Google Drive folder (`EAG SF 2026/`) | Typed notes: Anshul, Kushal, Marius, Diogo, Juan Felipe, Mike M, Ron, Tomas, "matt; j" | 9 note files |
| Google Drive folder | 3 HEIC images (IMG_2456-2458) — likely handwritten notes | 3 images |
| People Database (Google Sheet) | Existing contacts with 19-column schema | ~300 rows |

## Step-by-Step Execution

### Step 1: Build Master Contact Table
1. **Extract from Swapcard screenshots** (already parsed from images):
   - All 34 contacts with name, title, org, date, time
2. **Cross-reference with Google Calendar** to catch additional contacts not in Swapcard:
   - Katherine Biewer (2 meetings), Julie Steele, Cameron Berg, Govind, Anish Mohammed
3. **Save Swapcard images** to `~/build/luthien-org/ui-fb-dev/0-outreach4feedback/` (user requested)
4. **Output**: Markdown table with ~39 contacts, shown to Scott for review

### Step 2: Match Sources to Each Contact
For each contact, match:
- **Otter transcript** — by name + date/time overlap (21 transcripts available Feb 13-15)
- **Drive notes** — by filename match (9 typed notes + 3 HEIC handwritten images)
- **Calendar details** — location, description text from Swapcard

**Known transcript matches** (from Otter list):
| Contact | Otter Transcript ID | Duration |
|---------|---------------------|----------|
| Matt Brooks | BKrGUmVCqf1A0o3MmiPJRbWg_sc | 58m |
| Lindley Lentati | 0dr-3DIAz031NbtlHAGITmHRuPw | 1h 20m |
| Max Werner | URQngfXAw74Cz8LF5OSyaoj3E5c | 26m |
| Dylan Fridman | ql8jIJog6fhrPW6-2zm5kv_eiY8 | 25m |
| Marius Hobbhahn | WUkUwGa27n9bTVIUytoSfgY5YHo | 29m |
| Anshul Khandelwal | qeIh_-VDXF7GDcVh20htpHL47og | 20m |
| Kushal Agrawal | zzDZN_eUiqwZAreRsmOGdDaT4aQ | 23m |
| Aaron Sandoval | c5jxUdUzQFRcy2fvsJjwn3yNycg | 22m |
| Luis Slyfield | 8c8z4QZfiILa_X06J_YSztUoCfc | 20m |
| Felix Hofstätter | QTSyNYAS5iO7zQgcT8h4qDPT5lc | 28m |
| Ardy Haroen + Lindley | 0371qaxrGXn33RUmuqv3_mwDnvw | 57m |
| Tomáš Turlík | OuHTjDDkpIhdvUIZHXgh7EQ75YA | 24m |
| Mike Mantell | ZWXR8NrFer_l8INl1etnwa19_Ec | 1h 43m |
| Matt Handzel | UVZXY3twpv04x-IQ04BCunX8ZLg | 24m |
| Govind | I-FhxBhHugYLbHwVs9O_mKBywgA | 18m |
| Anish Mohammed | NVOJp2Q_NXCAf55Ndp47RvSVQRk | 29m |

**Unmatched transcripts** to investigate:
- "AI Safety Workflow Review" (Feb 14 9:37 AM, 2h 54m) — long session, may cover Martin Leitgab + Grace Roberts block
- "Product Feedback and Strategy" (Feb 14 1:29 PM, 30m) — likely Marcus Abramovitch or Adam Tury slot
- "AI Code Compliance Strategy" (Feb 13 3:16 PM, 39m) — likely Benjamin Hodgkiss slot
- "Security and AI Strategy Meeting" (Feb 13 2:37 PM, 14m) — overlaps with Govind time
- "Seldon Storm Lightning Talks" (Feb 13 1:44 PM, 37m) — event, not 1:1

**Known Drive notes matches:**
- Anshul.md → Anshul Khandelwal
- Kushal.md → Kushal Agrawal
- Marius.md → Marius Hobbhahn
- Diogo:.md → Diogo de Lucena
- Juan at openai.md → Juan Felipe Ceron Uribe
- Mike M.md → Mike Mantell
- Ron.md → Ron Bobrov
- Tomas.md → Tomáš Turlík
- matt; j.md → Matt Handzel + Julian Stastny (combined)

**3 HEIC images** (IMG_2456-2458): Can't read HEIC in this environment. Will note them as unprocessed handwritten notes for Scott to match manually.

**Show matching table to Scott before proceeding** (per user's request).

### Step 3: Extract Takeaways & Action Items
For each matched contact, pull from Otter transcript + Drive notes:
- **Key discussion topics**
- **Their frustrations / needs** (relevant to Luthien)
- **Action items** (who owes what)
- **Follow-up interest level**

Method: Use `otter_get_transcript` for each matched transcript, extract relevant sections. Combine with Drive notes. Show summary table to Scott before proceeding.

### Step 3.5: Flag High-Priority Contacts
Flag anyone who:
- Expressed interest in Luthien + willingness for follow-up call
- Mentioned recurring calls (bonus: biweekly)
- Active collaboration interest

**Already-known high-priority from notes:**
- **Marius Hobbhahn** (Apollo Research) — notes say "Call next week: Marius + Scott required, Jai, Jeremy, Marcus optional"
- **Lindley Lentati** (Cambridge Inference) — had 1h20m + 57m meetings, collaboration on multi-agent stuff
- **Tomáš Turlík** — notes say "I'd like to try Luthien"
- **Diogo de Lucena** (AE Studio) — "send readme and he will post in internal AE Studio slack"
- **Ron Bobrov** — "send theory of change" + "send scott's articulation of ron's critiques"

### Step 4: Save & Update
1. **Save markdown** to `~/build/luthien-org/ui-fb-dev/0-outreach4feedback/eag-sf-2026/eag-sf-contacts.md`
   - Full contact table with all columns
   - Per-person sections with takeaways, action items, priority flag
2. **Update People Database** Google Sheet via `mcp__gdrive__append_to_sheet`
   - Only add NEW contacts not already in the sheet
   - Match existing columns: Name, Title/Role, Organization, Notes, Last Contacted, Next Follow-Up, Priority, Status, Design Partner?

## Key Files
- **Output**: `~/build/luthien-org/ui-fb-dev/0-outreach4feedback/eag-sf-2026/eag-sf-contacts.md`
- **Images saved to**: `~/build/luthien-org/ui-fb-dev/0-outreach4feedback/eag-sf-2026/`
- **Existing context**: `~/build/luthien-org/ui-fb-dev/0-outreach4feedback/eag-sf-2026/eag-sf-outreach-context.md`
- **Drive notes**: `~/build/luthien-org/luth-gdrive-clone/Conferences/EAG SF 2026/`
- **People DB**: Google Sheet `1lKNWdLRrkRu4VtxLsdWnKF_OFPBXAgG1aMioS9shHSM`

## Verification
- Review matching table with Scott at Step 2 checkpoint
- Review takeaways with Scott at Step 3 checkpoint
- Verify People Database append didn't duplicate entries
- Confirm markdown file renders correctly

## Limitations
- 3 HEIC handwritten note images can't be read programmatically — will flag for Scott to process manually
- Some Otter transcripts have generic titles ("AI Safety Workflow Review") — will match by timestamp
- Some contacts may not have any transcript or notes (e.g., Grace Roberts, Aaron Hamlin, Reshma Kosaraju)
