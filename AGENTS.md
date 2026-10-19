## User-documentation context

The User-Documentation manager reviews merged product pull-request diffs,
verifies relevant source and UI behavior, and owns Help content, editorial
decisions, and the documentation backlog. Development sessions do not need to
run documentation tools, create evidence JSON, open paired documentation pull
requests, or access the private `wxk-support` repository to deliver product work.

When useful, a session can add a brief note to the ordinary handoff or pull
request with changed behavior, exact English UI labels, and known limitations.
This context is optional and is not a delivery gate. The central
[User-Documentation contract](https://github.com/GilbertoAbrao/wxk-support/blob/main/documentation/README.md)
remains the manager's reference. This policy supersedes the previous
`begin`/`check` session gates, including for sessions already in progress.

## Worktree Cleanup on Completion

Disk on the development Macs is finite; abandoned worktrees filled the
MacBook Air to 100% on 19/10/2026. Every session that creates a Git worktree
removes it when its work is concluded:

1. Concluded means the branch is pushed and its pull request is merged or
   closed, or the work was abandoned with nothing left to keep.
2. Confirm the worktree is clean and has no unpushed commits:
   `git -C <wt> status --porcelain` is empty and
   `git -C <wt> rev-list --count HEAD --not --remotes` is `0`.
3. Remove it from the main checkout: `git worktree remove <wt>`, then
   `git worktree prune`. Keep the branch unless the project's rules say to
   delete merged branches.
4. Never remove a worktree with uncommitted changes, unpushed commits, or a
   local database (for example `.data/*.db`); report it in the handoff
   instead.

A session's final report states the removed worktree path, or why it was kept.
