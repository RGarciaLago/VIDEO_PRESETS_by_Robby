# [VIDEO PRESETS by Robby] for [MiSTer Platform](https://github.com/MiSTer-devel/Main_MiSTer/wiki)
These are video preset files that you can use to fully configure a core's video settings. The intention with these presets is to provide an idealized version how a game platform's visuals appeared when it was new and to provide a starting point to make your own. Have fun!


## Installation
Download all presets (https://github.com/RGarciaLago/VIDEO-PRESETS-by-Robby/tree/main/Presets) to the `/media/fat/Presets/` folder on your SD card.

### Updates
You can automatically download and get latest with the MiSTer update script (and update_all) by adding the following text to the `/media/fat/downloader.ini` file:
```ini
[VIDEO-PRESETS-by-Robby]
db_url = https://raw.githubusercontent.com/RGarciaLago/VIDEO-PRESETS-by-Robby/db/db.json.zip
```

## Usage
Once you've installed all presets you can apply them by following these instructions:
1. Within any Core, press your menu button to bring up the Core menu, then push right to view the `System` menu.
2. In the System menu, select the `Video processing` option.
3. Within Video processing select the top option called `Load preset`.
4. You can now select whichever preset that works for the Core you're using.


### General Presets
These aren't specific to a single core but meant to be applied to game platforms that are similar or are from the same time period.

Arcade presets are available for horizontal monitors, vertical monitors, and vector displays. There's a single Computer preset (for now) and game consoles have their presets separated into hardware generations (https://en.wikipedia.org/wiki/Home_video_game_console_generations) to reflect display technology of the time.

### Core Specific Presets
All handhelds, or consoles with a unique display method, feature specific presets due to the quirks of their display. These are intended to work at any resolution or scaling method applied.

Some handhelds have had presets with shadow masks created for them so these are provided as optional within the "With Shadow Masks" folder. Use v-integer scaling with any presets that have shadow masks so they remain aligned with the handheld's pixel dimensions.
