# cl0ud — Poster & Physical Plinth Attribution Snippets

> **System Designation:** Physical Plinth & Poster Typography Snippets  
> **Brand Mark:** cl0ud  
> **Specification Reference:** [`cl0ud-brand-spec.json`](file:///Users/roopalisingh/Desktop/cl0ud/cl0ud-brand-spec.json)

---

## 1. Physical Machine Plinth Layout (Acrylic / 3D Print / Metal)

For physical hardware displays (e.g. quadruped chassis, mobile dustbin, hydroponic station), fabricate a $60\text{mm} \times 20\text{mm}$ plate using [`assets/badges/exhibition-plinth-badge.svg`](file:///Users/roopalisingh/Desktop/cl0ud/assets/badges/exhibition-plinth-badge.svg) or laser-etch the following typography:

```
┌────────────────────────────────────────────────────────────────────────┐
│  [ cl0ud ]  SYSTEMS ARCHITECTURE POWERED BY cl0ud                     │
│             CO-ENGINEERED BY OJAS SINGH                                │
│             DPSI STUDENT ROBOTICS & AUTONOMOUS SYSTEMS LAB             │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Exhibition Poster Footer Block (LaTeX / InDesign / Illustrator)

### Plain Text Box (Bottom Center or Bottom Right, 14pt min)
```text
SYSTEMS ARCHITECTURE: Powered by cl0ud
CO-ENGINEERED BY: Ojas Singh
CORE ROBOTICS TEAM: DPSI Student Robotics Team
ACADEMIC INSTITUTION: Delhi Public School Indirapuram (DPSI)
MONOGRAPH SPECIFICATION: Rev 5.0.0 (https://github.com/Ojas-sta)
```

### LaTeX Beamer / Poster Snippet
```latex
\begin{block}{Engineering Credits \& Attribution}
  \textbf{Systems Architecture:} Powered by \texttt{cl0ud} \\
  \textbf{Lead Co-Engineer:} Ojas Singh (\texttt{ojasctc@gmail.com}) \\
  \textbf{Project Team:} DPSI Student Robotics Team \\
  \textbf{Institutional Support:} Advanced Prototyping Laboratory, DPS Indirapuram
\end{block}
```
