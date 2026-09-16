# ACIR Learning Kits - Characterization & Experimentation Platform

**Decibels Lab Pvt Ltd**  
*Project Repository: [ACIR-Learning-Kit-1-PCB](https://github.com/P-Shreyas543/ACIR-Learning-Kit-1-PCB)*  
*Revision: v2.0 | Date: 2026-09-16*

---

## Overview

The **ACIR Learning Kits** are specialized, production-ready characterization platforms designed for educational, research, and laboratory electrochemical impedance spectroscopy (EIS) and AC internal resistance (ACIR) testing of 18650 lithium-ion cells.

Each kit integrates three distinct battery testing configurations:
1. **1S 1P Baseline Cell**: Individual 18650 cell baseline ACIR characterization.
2. **1S 4P Parallel Pack**: Four-cell parallel module for current-sharing, contact resistance, and parallel cell mismatch studies.
3. **4S 1P Series String**: Four-cell series string for cumulative pack impedance, inter-cell busbar resistance, and per-cell probing.

---

## Repository Structure

The workspace is organized into dedicated project directories for each learning kit:

```
c:/Users/Shreyas/Documents/ACIR_PCB/
├── README.md                                  # Workspace Platform Documentation
├── .gitignore                                 # Git Ignore Configuration
├── ACIR-Learning-Kit-1-PCB/                   # Learning Kit 1 Project Directory
│   ├── ACIR-Learning-Kit-1-PCB.kicad_pro      # KiCad 10 Project File
│   ├── ACIR-Learning-Kit-1-PCB.kicad_pcb      # 2-Layer PCB Layout File
│   ├── ACIR-Learning-Kit-1-PCB.kicad_sch      # Complete Schematic Design
│   ├── ACIR-Learning-Kit-1-PCB.kicad_prl      # User Settings & Display Cache
│   ├── ACIR-Learning-Kit-1-PCB_BOM.csv        # Bill of Materials
│   ├── ACIR-Learning-Kit-1-PCB_LAYOUT.pdf     # Vector Layout Drawing
│   ├── ACIR-Learning-Kit-1-PCB_SCH.pdf        # Vector Schematic Drawing
│   ├── ACIR-Learning-Kit-1-PCB-drc.rpt        # DRC Verification Report (0 violations)
│   ├── ACIR-Learning-Kit-1-PCB-erc.rpt        # ERC Verification Report (0 errors)
│   ├── fp-lib-table                           # Footprint Library Table
│   ├── footprints.pretty/                     # Project Footprint Library
│   ├── gerbers/                               # RS-274X Gerbers & Drill Files
│   └── production/                            # JLCPCB Fabrication Deliverables
│       ├── ACIR-Learning-Kit-1-PCB_gerbers.zip# Complete Fabrication Archive
│       ├── ACIR-Learning-Kit-1-PCB_LAYOUT.pdf # Layout Drawing PDF
│       ├── ACIR-Learning-Kit-1-PCB_SCH.pdf    # Schematic Drawing PDF
│       ├── bom.csv                            # Component BOM
│       ├── positions.csv                      # Centroid Component Placement
│       └── netlist.ipc                        # IPC-D-356 Test Netlist
│
└── ACIR-Learning-Kit-2-PCB/                   # Learning Kit 2 Project Directory
    ├── ACIR-Learning-Kit-2-PCB.kicad_pro      # KiCad 10 Project File
    ├── ACIR-Learning-Kit-2-PCB.kicad_pcb      # 2-Layer PCB Layout File
    ├── ACIR-Learning-Kit-2-PCB.kicad_sch      # Complete Schematic Design
    ├── ACIR-Learning-Kit-2-PCB.kicad_prl      # User Settings & Display Cache
    ├── ACIR-Learning-Kit-2-PCB_BOM.csv        # Bill of Materials
    ├── ACIR-Learning-Kit-2-PCB_LAYOUT.pdf     # Vector Layout Drawing
    ├── ACIR-Learning-Kit-2-PCB_SCH.pdf        # Vector Schematic Drawing
    ├── ACIR-Learning-Kit-2-PCB-drc.rpt        # DRC Verification Report (0 violations)
    ├── ACIR-Learning-Kit-2-PCB-erc.rpt        # ERC Verification Report (0 errors)
    ├── fp-lib-table                           # Footprint Library Table
    ├── footprints.pretty/                     # Project Footprint Library
    ├── gerbers/                               # RS-274X Gerbers & Drill Files
    └── production/                            # JLCPCB Fabrication Deliverables
        ├── ACIR-Learning-Kit-2-PCB_gerbers.zip# Complete Fabrication Archive
        ├── ACIR-Learning-Kit-2-PCB_LAYOUT.pdf # Layout Drawing PDF
        ├── ACIR-Learning-Kit-2-PCB_SCH.pdf    # Schematic Drawing PDF
        ├── bom.csv                            # Component BOM
        ├── positions.csv                      # Centroid Component Placement
        └── netlist.ipc                        # IPC-D-356 Test Netlist
```

---

## PCB Specifications (Both Kits)

- **Dimensions**: $297.0\text{ mm} \times 210.0\text{ mm}$ (Standard A4 Landscape)
- **Layer Count**: 2 Layers ($1\text{ oz}$ / $35\,\mu\text{m}$ copper per layer)
- **Board Thickness**: $1.6\text{ mm}$ FR-4
- **Surface Finish**: HASL / ENIG compatible
- **Power Bus Tracks**: $8.0\text{ mm}$ width with 6-row dense stitching via matrices ($0.8\text{ mm}$ diameter, $0.4\text{ mm}$ drill)
- **Test Points**: 20 SMD pads ($2.0\text{ mm}$ pad diameter, $6.0\text{ mm}$ solder mask opening) with centered $0.8\text{ mm}$ probe-grip through-via
- **Fabrication Standards**: Verified 100% compliant with JLCPCB 2-layer fabrication capabilities (0 DRC violations, 0 ERC errors)

---

## Design Team
- **Ashutosh Raj**
- **Shreyas P**
- **Suraj S D**
