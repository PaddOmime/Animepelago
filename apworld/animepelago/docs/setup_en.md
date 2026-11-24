# Animepelago Setup Guide

## What you need

- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases) **0.6.8 or newer** (only for generating –
  you play in the browser).
- `animepelago.apworld` and `Animepelago.yaml` from the
  [Animepelago releases](https://github.com/PaddOmime/Animepelago/releases).
- A browser (PC or phone). Nothing else to install: the game runs at
  **<https://paddomime.github.io/Animepelago/client/>**.

## 1. Install the APWorld

Double-click `animepelago.apworld` (the Archipelago Launcher installs it), or copy it into the `custom_worlds`
folder of your Archipelago installation. Restart the Launcher afterwards.

## 2. Create your YAML

- Take `Animepelago.yaml` from the release (or use the **📄 Download Animepelago.yaml** button in the web client),
  or create one with the **Options Creator** in the Archipelago Launcher.
- Set your `name` and adjust the options. Every option is explained in the file; the most important ones are
  `anime_count`, `anime_goal`, `unlock_mode`, `genre_rule` and `title_language`.

## 3. Generate and host

Put all YAMLs of your group into the `Players` folder and run **Generate** in the Launcher, then upload the result
to [archipelago.gg/uploads](https://archipelago.gg/uploads) to host the room.
Hosting on archipelago.gg is the easiest way (see "Local servers" below).

## 4. Connect and play

1. Open **<https://paddomime.github.io/Animepelago/client/>**.
2. On the **Archipelago** tab enter the server (e.g. `archipelago.gg`), the port of your room, your slot name and,
   if set, the password. Then press **Connect**.
3. Type anime titles into the guess field. Any known title counts (English, Romaji, Japanese, German, Spanish,
   French, Italian), small typos are fine. Locked anime show which items they still need.
4. Chat and commands (e.g. `!hint`) go into the message field at the bottom.

The client remembers your connection data. If the connection drops it reconnects by itself; progress that wasn't
sent yet is sent afterwards.

## Local servers

The web client runs on https, so browsers only allow it to open **encrypted** connections (`wss://`).
Rooms on archipelago.gg support that. A server on your own PC usually doesn't – then download the client
(the `client` folder from the repository) and open `index.html` locally.

## Good to know

- **DeathLink / TrapLink:** switch them on with `death_link` / `trap_link` in your YAML.
- **Collect:** if another player collects their items from your world, those anime are marked 📦. A switch in the
  client decides whether they count towards your goal.
- **Twitch chat**: with the Twitch button your chat can guess along. Agree with your multiworld first
  whether that is OK.
- **Profiles:** create a profile (👤) and choose a route – then your Archipelago games also give XP and achievements.
- **Problems or ideas?** Open an issue on [GitHub](https://github.com/PaddOmime/Animepelago/issues).
