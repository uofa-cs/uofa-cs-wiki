# Tools and Setup

What the department and university give you, and where to learn the rest. Generic setup advice (editors, dotfiles, shell themes) is a search away; this page sticks to what's specific to being a UofA CS student.

---

## Department Machines

Your CS account uses your CCID ([CCIDs in Computing Science](https://www.ualberta.ca/en/computing-science/resources/technical-support/account-information/ccids-in-computing-science.html)).

| What | Details |
|---|---|
| Remote login for undergrads | `ssh yourccid@ohaton.cs.ualberta.ca`. The [SSH page](https://www.ualberta.ca/en/computing-science/resources/technical-support/networks/remote-access-ssh.html) recommends it because it has extended-hours support. |
| What ohaton is for | It's the [undergraduate gateway](https://www.ualberta.ca/en/computing-science/resources/technical-support/computing-resources/index.html) to the department (Ubuntu 20.04). Don't run long or CPU-heavy jobs on it. |
| Lab machines | Linux workstations in UCommons rooms 2030, 2070, 2086, 2130, 2140, 3130, and 3140, named like `ucomm-2086-w05` ([full list](https://www.ualberta.ca/en/computing-science/resources/technical-support/computing-resources/index.html)). |
| Copying files | `scp` is the department's [preferred method](https://www.ualberta.ca/en/computing-science/resources/technical-support/networks/remote-access-ssh.html) for moving files to and from your CS account. |

If a course outline names a marking environment, test there before you submit, even if your laptop runs a similar OS.

### VPN

The department's [VPN page](https://www.ualberta.ca/en/computing-science/resources/technical-support/networks/vpn.html) (`vpn.ualberta.ca/cs`, CCID plus Duo) is for the CS Intranet, shared drives, and printers, and is aimed at people with a direct relationship with the department such as faculty and grad students. The SSH page doesn't list it as a requirement for reaching ohaton.

### Compute and GPUs

The department doesn't publish any GPU or cluster access for undergrads. If you need serious compute for research, ask your supervisor; see [Getting into Research](../research/getting-into-research.md).

---

## Free Software

| Offer | How to get it |
|---|---|
| [GitHub Student Developer Pack](https://education.github.com/pack) | Verify with your UofA email. As of October 2026 it includes Copilot Student, GitHub Pro, Codespaces at Pro level, $100 Azure credit, $50 MongoDB Atlas credit, a free `.me` domain from Namecheap for a year, and Heroku credit. |
| [JetBrains IDEs](https://www.jetbrains.com/academy/student-pack/) | Free with a student email, renewed yearly (also listed in the GitHub pack). |
| [Microsoft 365](https://ualberta.onthehub.com/WebStore/OfferingDetails.aspx?o=44f9873d-b9d3-e811-810b-000d3af41938) | Free Office apps for UofA students through the university's OnTheHub store. |
| Microsoft developer software | The department's [software page](https://www.ualberta.ca/en/computing-science/resources/technical-support/software.html) lists Visual Studio and other Microsoft dev tools for students in a CMPUT course, also through [OnTheHub](https://ualberta.onthehub.com/). |

If you're on Windows, install [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) so you have the same Unix tools as the lab machines. Several courses assume Linux: 274 is developed on Linux, 201 uses the Unix toolchain, and 404's [marking environment](https://uofa-cmput404.github.io/general/environment.html) is Ubuntu.

---

## Learning Git and the Terminal

201 introduces the Unix toolchain and 301 uses revision control, but you'll want more fluency than either gives you. Pick one from each line:

- **Terminal and tooling:** [The Missing Semester of Your CS Education](https://missing.csail.mit.edu) (MIT)
- **Git, interactively:** [Learn Git Branching](https://learngitbranching.js.org)
- **Git, in depth:** [Pro Git](https://git-scm.com/book/en/v2) (free book)

For what the courses do and don't cover, see the [Curriculum Map](curriculum-map.md).

*Last verified: October 2026.*
