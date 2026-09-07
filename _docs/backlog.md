# Household Chore Tracker — Django Backlog

Builds on `_docs/plan.md`. The original plan assumed browser localStorage
with no backend; this backlog re-targets that same scope onto Django
models + a database (SQLite) instead, keeping every functional
requirement intact: logging completions with timestamps, free add/edit/
remove of chores, a per-chore interval, overdue flagging, and a
mobile-friendly single page.

## Tasks

1. **Define the Chore and LogEntry models**
   Add a `Chore` model (name, interval in days) and a `LogEntry` model
   (foreign key to Chore, timestamp of completion) to `chores/models.py`,
   matching the data model in plan.md but backed by the database instead
   of localStorage.
   *Done when:* both models are defined with appropriate fields/relations
   and `python manage.py makemigrations` produces a clean migration with
   no errors.

2. **Run migrations and wire up the admin**
   Apply the migration to create the SQLite tables, then register both
   models in `chores/admin.py` so they're usable from Django admin.
   *Done when:* `python manage.py migrate` succeeds, a superuser can log
   in to `/admin/`, and Chores and LogEntries can be created/viewed/
   edited/deleted there.

3. **Manual smoke test via admin**
   Using only the admin, create a few chores with different intervals
   and add some log entries (including some with old timestamps) to
   confirm the data model actually supports the intended behavior.
   *Done when:* a handful of chores and log entries exist in the DB and
   look correct when inspected via admin.

4. **Add the chore list view (read-only)**
   Add a view + URL that lists all chores, each showing its name,
   interval, and most recent log entry timestamp (if any), rendered with
   a basic template. No overdue logic yet.
   *Done when:* visiting the app's root URL shows all chores from the DB
   with their last-done time (or "never").

5. **Add overdue flagging logic**
   Compute, per chore, whether time since its most recent log entry
   exceeds its interval (or if it has never been logged), and surface
   that as an "overdue" flag in the list view.
   *Done when:* the chore list visibly distinguishes overdue chores from
   up-to-date ones, verified against the test data from task 3.

6. **Add "log completion" action**
   Add a button/link per chore on the list page that creates a new
   LogEntry for that chore with the current timestamp (a simple POST
   view), then redirects back to the list.
   *Done when:* clicking "Done" on a chore creates a log entry with
   now's timestamp and the list updates (overdue flag clears, last-done
   time updates) without using the admin.

7. **Add chore management (create/edit/delete)**
   Add views + forms (can use Django's generic CRUD views or plain
   function views) so chores can be added, edited, and removed directly
   from the app, not just via admin.
   *Done when:* a user can add a new chore, change its name/interval, and
   delete a chore, all from the web page.

8. **Single-page mobile-friendly layout**
   Consolidate the chore list + add/edit forms + log-completion actions
   onto one main page (using partial templates/includes as needed), and
   apply basic responsive CSS so it's usable on a phone-sized screen.
   *Done when:* all core actions (view chores, see overdue status, log a
   completion, add/edit/remove a chore) are reachable from a single page
   that renders cleanly at mobile widths.

9. **Polish and edge cases**
   Handle small gaps: empty state (no chores yet), confirmation before
   deleting a chore, basic input validation (e.g. interval must be a
   positive number), and any obviously rough UI spots.
   *Done when:* the app behaves sensibly with zero chores, rejects
   invalid interval input, and deleting a chore requires confirmation.
