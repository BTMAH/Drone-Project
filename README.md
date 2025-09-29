# Drone Project

This repository documents the development, configuration, and future planning for my custom FPV drone build.  
It includes firmware configuration backups, STM32 embedded development, and a roadmap for transitioning from manual flight to autonomous missions.

---

## 1. STM32CubeIDE Development
The `STM32CubeIDE` directory contains work related to my **custom STM32-based expansion board**.  
This board is intended to provide extra I/O and accessory support beyond what my current flight controller can handle.  
Future development will focus on integrating sensors and additional features that expand the drone’s overall capabilities.

---

## 2. Betaflight Configurations
The `Betaflight Settings` folder stores **CLI dumps and diffs** exported directly from Betaflight Configurator.  
These represent my current efforts to fully optimize flight performance in **manual/FPV mode**.  
By version-controlling these settings, I can safely experiment, roll back changes, and track the evolution of my tuning over time.

---

## 3. Transition to ArduPilot
Once Betaflight is fully optimized, I plan to **switch the firmware to ArduPilot**.  
ArduPilot offers autonomous mission capabilities (e.g., GPS waypoints, return-to-home, and autonomous path following).  
This transition will allow me to move beyond FPV/manual flying into **autonomous mission testing**.

---

## 4. Current Drone Status
- ✅ Drone is **fully functional in manual/FPV mode** under Betaflight.  
- 🔧 Actively tuning and logging CLI dumps.  
- 🚀 Future plan: flash ArduPilot and enable **autonomous small-scale missions**.  

## 5. Project Scope & Future Plans
Because this build is based on a compact 3" frame, it is not designed to carry the extra compute and sensors required for full obstacle-aware autonomy.  

Instead, the near-term goal is to enable **autonomous waypoint missions** via ArduPilot.  
Looking further ahead, I plan to scale this work into a larger platform capable of carrying more advanced hardware for **full autonomous navigation**.

---

## Notes
This repo serves as a **living logbook** of both configuration and development.  
- For Betaflight pilots: check the `Betaflight Settings` folder to see current and past CLI dumps.  
- For embedded devs: see the `STM32CubeIDE` folder for firmware/board work.  
