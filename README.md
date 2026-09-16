# ACIR Learning Kit 1 - Characterization & Experimentation Board

**Decibels Lab Pvt Ltd**  
*Project Repository: [ACIR-Learning-Kit-1-PCB](https://github.com/P-Shreyas543/ACIR-Learning-Kit-1-PCB)*  
*Revision: v2.0 | Date: 2026-09-16*

---

## Overview

The **ACIR Learning Kit 1** is a specialized, production-ready characterization platform designed for educational, research, and laboratory electrochemical impedance spectroscopy (EIS) and AC internal resistance (ACIR) testing of 18650 lithium-ion cells.

The board integrates three distinct battery testing configurations:
1. **1S 1P Baseline Cell**: Individual 18650 cell baseline ACIR characterization.
2. **1S 4P Parallel Pack**: Four-cell parallel module for current-sharing, contact resistance, and parallel cell mismatch studies.
3. **4S 1P Series String**: Four-cell series string for cumulative pack impedance, inter-cell busbar resistance, and per-cell probing.

---

## Repository Structure

All active KiCad design files, footprint libraries, and manufacturing deliverables are organized in the [`ACIR-Learning-Kit-1-PCB/`](file:///c:/Users/Shreyas/Documents/ACIR_PCB/ACIR-Learning-Kit-1-PCB/) directory:

```
ACIR-Learning-Kit-1-PCB/
├── ACIR-Learning-Kit-1-PCB.kicad_pro       # Main KiCad 10 Project File
├── ACIR-Learning-Kit-1-PCB.kicad_pcb       # 2-Layer PCB Layout File
├── ACIR-Learning-Kit-1-PCB.kicad_sch       # Complete Schematic Design
├── ACIR-Learning-Kit-1-PCB.kicad_prl       # User Configuration Settings
├── ACIR-Learning-Kit-1-PCB_BOM.csv         # Bill of Materials (BOM)
├── ACIR-Learning-Kit-1-PCB_LAYOUT.pdf      # Complete Board Layout Vector PDF
├── ACIR-Learning-Kit-1-PCB_SCH.pdf         # Schematic Vector PDF
├── ACIR-Learning-Kit-1-PCB-drc.rpt         # KiCad Official DRC Report (0 violations)
├── ACIR-Learning-Kit-1-PCB-erc.rpt         # KiCad Official ERC Report (0 errors)
├── fp-lib-table                            # Local Footprint Library Table
├── footprints.pretty/                      # Project Footprint Library
├── gerbers/                                # Complete RS-274X Gerbers & Drill Files
└── production/                             # Manufacturing Deliverables for Fabrication
    ├── ACIR-Learning-Kit-1-PCB_gerbers.zip # Fabrication Archive (JLCPCB 2-Layer Ready)
    ├── ACIR-Learning-Kit-1-PCB_LAYOUT.pdf  # Fabrication Layout PDF
    ├── ACIR-Learning-Kit-1-PCB_SCH.pdf     # Schematic PDF
    ├── bom.csv                             # Production BOM
    ├── positions.csv                       # SMD Centroid Component Positions
    └── netlist.ipc                         # IPC-D-356 Electrical Test Netlist
```

---

## PCB Specifications

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
