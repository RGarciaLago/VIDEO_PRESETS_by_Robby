# [VIDEO PRESETS by Robby] for the [MiSTer Platform](https://github.com/MiSTer-devel/Main_MiSTer/wiki)
These are video preset files you can use to easily configure a core's video settings. These presets present an idealized version how a game platform's visuals appeared when it was new and provides you a starting point to make your own presets. Have fun!



## Installation
Download [all presets](https://github.com/RGarciaLago/VIDEO-PRESETS-by-Robby/tree/main/Presets) to the `/media/fat/Presets/` folder on your SD card.

### Updates
You can automatically download and get latest with the MiSTer update script and [update_all](https://github.com/theypsilon/Update_All_MiSTer) by adding the following text to `/media/fat/downloader.ini`:
```ini
[RGarciaLago/VIDEO_PRESETS_by_Robby]
db_url = https://raw.githubusercontent.com/RGarciaLago/VIDEO_PRESETS_by_Robby/db/db.json.zip
```


## Usage
Once you've installed the presets you can apply them by following these instructions:
1. Within a core, press the menu button to bring up the Core menu, then push right to view the `System` menu.
2. In the System menu, select the `Video processing` option.
3. Within Video processing select the top option called `Load preset`.
4. Select any preset you'd like to apply and all Video processing options for that core will be updated.

### General Presets
These aren't specific to a single core but meant to be applied to game platforms that are similar or are from the same time period.

Arcade presets are available for horizontal monitors, vertical monitors, and vector displays. There's a single Computer preset (for now) and game consoles have their presets separated into [hardware generations](https://en.wikipedia.org/wiki/Home_video_game_console_generations) to reflect display technology of the time.

### Core Specific Presets
All handhelds (or consoles with a unique display method) have specific presets due to the quirks of their display. These are intended to work at any resolution or scaling method applied.


## More Resources
For more extensions and utilities to make your MiSTer even better go here: https://github.com/wizzomafizzo/mrext
