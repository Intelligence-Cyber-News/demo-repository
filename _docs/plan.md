# Household Chore Tracker — Scope

## Purpose
A tool for managing shared household chores, scoped for solo use as a
tracking log (not a scheduler/reminder system in the traditional sense).

## Who it's for
- Single user (just me).

## Core behavior
- It's a **tracking log**: record what chore was done and when, rather
  than pushing reminders.
- Each chore has its own **expected interval** (e.g. dishes = 1 day,
  vacuum = 7 days).
- A chore is flagged **overdue** when the time since its last logged
  entry exceeds its configured interval.

## Chore list management
- Chores can be **freely added, edited, and removed** at any time —
  no fixed upfront list.

## Platform
- A **simple, mobile-friendly web page** (not a CLI or desktop app).

## Data storage
- Stored in the **browser's localStorage**.
- Lives on a single device/browser — no backend, no database, no
  cross-device sync.

## Data model (draft)
- **Chore**: id, name, interval (days)
- **Log entry**: chore id, timestamp (date/time done)

## Open questions for v2 (not yet in scope)
- Categories/tags for chores
- Notes on individual log entries
- Editing or deleting past log entries
- Cross-device sync / backend storage
