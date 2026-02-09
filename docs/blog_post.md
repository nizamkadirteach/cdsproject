# Rethinking Assessment in the Age of AI: Building a Full-Stack App in Under an Hour

*By Nizam Kadir*

I’ve been reflecting a lot on how assessment fits into the AI-augmented learning landscape.

Recently, in under an hour, I was able to design and scaffold an entire project workflow using **Antigravity (Google)**—from ideation to structure to technical setup. By providing a clear project brief and constraints, I could observe how quickly complex artefacts could be generated, iterated, and refined with guided human judgement.

It even setup the GitHub repo as part of the project requirement, handling everything for me in minutes.

![CryptoPulse Dashboard](file:///Users/mohammadnizamabdulkadir/Library/CloudStorage/OneDrive-SingaporeUniversityofTechnologyandDesign/CDSProjects/docs/images/dashboard-live.png)
*The actual "CryptoPulse" application built during this session.*

This experience raised a bigger question for me as an educator:
**👉 What exactly are we assessing in the age of AI?**

If learners can now co-create artefacts rapidly with AI support, then product-centric assessment alone becomes increasingly fragile. The differentiator shifts towards:
✔️ **How students frame problems**
✔️ **How they make decisions**
✔️ **How they evaluate, refine, and justify outputs**
✔️ **How responsibly they use AI as a cognitive partner**

I’ve long believed that **process matters more than product**—and AI makes that distinction impossible to ignore. The challenge is not *whether* AI is used, but whether our assessment practices meaningfully capture learning, reasoning, and growth.

---

## 🛠️ The Process: From Prompt to Deployment

To demonstrate this "co-creation" speed, here is the actual workflow I used with the AI agent. Note how the role of the human shifts from *doing* the coding to *directing* the architecture and *validating* the quality.

### Phase 1: The "Blue Sky" Prompt
I started with a high-level, complex request. I didn't ask for a snippet; I asked for a *system*.

> **My Prompt:** "I want to create a multimodal sentiment and price analysis project for cryptocurrency... It needs to be a Streamlit app, use an LSTM model, and look 'premium' with a cyberpunk aesthetic. Also, generate a LaTeX report and presentation slides for me."

**The AI's Output:**
- Created the folder structure (`src/`, `data/`, `report/`, `slides/`).
- Wrote the Python ETL pipeline (`data_loader.py`, `preprocessing.py`).
- Built a PyTorch LSTM model (`model.py`).
- Drafted a skeleton LaTeX report.

### Phase 2: Iteration & Refinement (The "Human in the Loop")
The initial draft was functional but generic. This is where assessment must focus: *Critique*.

> **My Prompt:** "The UI text contrast is too low on the dark background. Fix the CSS. Also, the data isn't saving to disk—I need a script to ensure the raw and processed data is present for grading requirements."

**The AI's Output:**
- Wrote a custom `style.css` injection for the Streamlit app.
- Created `src/save_data.py` to fetch, clean, and save CSVs to a new `data/` directory.

### Phase 3: Rigor & Documentation
Moving from a "coding project" to an "academic submission."

> **My Prompt:** "Can you check and validate you have provided and done what the project requirements are? Verify the 'Full Marks' criteria. also can we do a user manual and a pipeline diagram?"

**The AI's Output:**
- Performed a self-audit against standard grading rubrics.
- Generated a **Mermaid.js** system architecture diagram.
- Wrote a `USER_MANUAL.md`.
- compiled the final PDF slides with the specific **SUTD Logo** branding I requested.

### Phase 4: Deployment
Usually a friction point for students, handled entirely by the agent.

> **My Prompt:** "Did you commit, stage, and push to GitHub?"

**The AI's Output:**
- Initialized the git repo.
- Created `.gitignore`.
- Pushed all code and large PDF assets to my remote repository: [nizamkadirteach/cdsproject](https://github.com/nizamkadirteach/cdsproject).

---

## 🧠 The Takeaway

The artifact above—a working ML app with professionally typeset documentation—was created faster than I could have written a traditional assignment brief.

If we grade only the *dashboard*, an AI can pass.
If we grade the *prompt engineering, the architectural decisions, the debugging of the specific logo issue, and the system verification logic*—that is where the human student shines.

I’m sharing this not as a critique, but as an invitation:
**👉 How are you rethinking assessment to stay aligned with how students actually learn today?**

Would love to hear perspectives from fellow educators, researchers, and practitioners navigating this shift.

---

### 📝 WordPress Metadata

**Categories:**
*   Artificial Intelligence in Education (AIEd)
*   EdTech & Learning Innovation
*   Higher Education
*   Computational Thinking

**Tags:**
*   Generative AI, Agentic Coding, Assessment Reform, Process vs Product, SUTD, Antigravity, Google DeepMind, Python, Streamlit, Pedagogy, Future of Work
