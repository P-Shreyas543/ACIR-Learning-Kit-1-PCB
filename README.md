# ACIR Learning Kits - Characterization & Experimentation Platform

**Decibels Lab Pvt Ltd**  
*Project Repository: [ACIR-Learning-Kit-1-PCB](https://github.com/P-Shreyas543/ACIR-Learning-Kit-1-PCB)*  
*Revision: v2.1 | Date: 2026-09-17*

---

## Overview

The **ACIR Learning Kits** are specialized, production-ready hardware characterization platforms designed for educational, research, and laboratory electrochemical impedance spectroscopy (EIS) and AC internal resistance (ACIR) testing of 18650 lithium-ion cells.

The repository contains two distinct learning kits:

### Learning Kit 1: Baseline Cell & Pack Topology Kit
1. **1S 1P Baseline Cell**: Single 18650 cell baseline ACIR characterization.
2. **1S 4P Parallel Pack**: Four-cell parallel module for current-sharing, contact resistance, and parallel cell mismatch studies.
3. **4S 1P Series String**: Four-cell series string for cumulative pack impedance and inter-cell busbar resistance.

### Learning Kit 2: Track Resistance & Interconnect Impedance Kit
1. **PCB Track Resistance Module**:
   - 3 calibrated test tracks with identical $6.0\text{ mm}$ width and varying lengths ($104.4\text{ mm}$, $58.0\text{ mm}$, $36.4\text{ mm}$).
   - Mirrored symmetrically on both copper layers (`F.Cu` and `B.Cu`).
   - Densely stitched with regular via matrices ($0.8\text{ mm}$ diameter, $0.4\text{ mm}$ drill).
   - Dedicated Kelvin test point probes: `P1` & `P2` (Track 1), `P3` & `P4` (Track 2), `P5` & `P6` (Track 3).
2. **4S 1P - (I) Module (Differential Cell ACIR Experiment)**:
   - 4 series cells (`BT2`, `BT3`, `BT4`, `BT5`) with uniform, ultra-low resistance interconnect buses ($8.0\text{ mm}$ 2-layer with dense via arrays).
   - Pack terminals: `B +ve` (BT2) and `B -ve` (BT5).
   - Students insert cells with *different* known ACIR values to observe that total pack ACIR is dominated by the sum of individual cell ACIRs when bus resistances are identical and negligible.
3. **4S 1P - (II) Module (Varying Interconnect Impedance Experiment)**:
   - 4 series cells (`BT6`, `BT7`, `BT8`, `BT9`) with deliberately *varying* interconnect track resistances:
     - **Link 1** (`BT6` $\leftrightarrow$ `BT7`): Ultra-wide $10.0\text{ mm}$ 2-layer bus with dense via matrix ($\approx 0.5\text{ m}\Omega$).
     - **Link 2** (`BT7` $\leftrightarrow$ `BT8`): Medium $3.0\text{ mm}$ single-layer trace ($\approx 3.0\text{ m}\Omega$).
     - **Link 3** (`BT8` $\leftrightarrow$ `BT9`): Narrow $0.8\text{ mm}$ single-layer trace ($\approx 10.0\text{ m}\Omega$).
   - Pack terminals: `B +ve` (BT6) and `B -ve` (BT9).
   - Students insert cells with *identical* ACIR values to demonstrate how interconnect trace impedance directly inflates total battery pack ACIR.

---

## Repository Structure

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
    ├── kit2_render_top.png                    # Photorealistic 3D Top Render
    ├── kit2_render_bottom.png                 # Photorealistic 3D Bottom Render
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
- **Fabrication Compliance**: Verified 100% compliant with JLCPCB 2-layer fabrication capabilities:
  - **DRC**: **0 violations**, **0 unconnected pads**
  - **ERC**: **0 violations**, **0 errors**, **0 warnings**

---

## Design Team
- **Ashutosh Raj**
- **Shreyas P**
- **Suraj S D**
