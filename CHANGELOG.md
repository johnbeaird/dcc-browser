# Changelog

All notable changes to Dungeon Crawler Carl: The Browser Incident will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2026-02-03 - "The Awakening"

### Added
- **6 Themed Room Templates**: Treasure Vault, Ancient Crypt, Throne Room, Prison Cells, Forbidden Library, plus 5 geometric layouts
- **8 New Enemy Types**:
  - Slime 🟢 - Splits into 2 smaller slimes on death
  - Skeleton 💀 - Revives once after 3 seconds at 50% HP
  - Spider 🕷️ - Fast dasher that leaves web traps
  - Ogre 🧌 - Tank that throws rocks from distance
  - Ghost 👻 - Phases through walls, teleports
  - Assassin 🗡️ - Circles for backstab bonus damage
  - Shaman 🔮 - Buffs allies, ranged magic
  - Hound 🐕 - Pack hunter, howls to wake enemies
- **Proximity-Based Enemy AI**: Enemies start sleeping, wake when player approaches (250-350px range)
- **Advanced AI Behaviors**:
  - Pack tactics (Hound calls for help)
  - Ally buffs (Shaman speed boost)
  - Positional tactics (Assassin backstabs)
  - Death mechanics (Slime split, Skeleton revive)
  - Terrain interaction (Ghost wall phasing)
- Visual sleep indicators (Z) and wake-up alerts (!)
- Progressive AI states: sleeping → lurking → stalking → attacking

### Changed
- Increased combat rooms per floor from 2-3 to 2-4 based on depth
- Updated Arrow class to support custom damage and sprites
- Total room pool expanded to 12 unique layouts

### Removed
- Debug visualizations (door trigger circles, position overlay)

## [0.2.0] - 2026-02-03 - "Room Cards"

### Added
- **Room-Based Dungeon System**: Procedurally generated floors with connected rooms
- **12 Room Templates**: Start chamber, combat rooms, safe room (Prancing Princess), boss arena, exit stairwell
- **Wall Collision System**: Solid walls with proper circle-rectangle collision detection
- **Door System**: Visual teleport triggers with 100px activation radius
- **Room Transitions**: Smooth camera follow, grace period invulnerability
- **Mini-Map**: Shows explored rooms and current position
- **Room Modifiers**: Darkness, Flood, Audience Favorite, Blood Moon

### Fixed
- Vector2 mutation bug in wall collision pushOut method
- Position limit increased from 2000 to 10000 for multi-room dungeons
- Wall gaps removed, doors converted to teleport triggers
- Room transition cooldown prevents door bouncing

### Changed
- Converted from single arena to multi-room dungeon progression
- Enemies now spawn inside rooms with strategic placement
- Player spawns at room center on transition

## [0.1.0] - 2026-01-XX - "Arena Prototype"

### Added
- Initial wave-based arena combat system
- Player (Carl) and companion (Donut) with basic stats
- 5 Enemy types: Goblin, Bat, Kobold, Boss, Mimic
- Inventory system: Bombs, Potions, Traps, Steroids
- Achievement system with 10+ achievements
- Live chat simulation with viewer interactions
- Boss fights every 3 waves
- Safe room vendor (Prancing Princess)
- Audio system with procedural sound effects
- Touch controls and mobile support
- CRT monitor visual effects

### Core Systems
- HTML5 Canvas rendering
- Vanilla JavaScript (no external libraries)
- Entity-Component architecture
- Real-time physics and collision
- Achievement tracking
- XP and leveling system
- Score and viewer count systems

---

## Version Naming Scheme

Versions follow semantic versioning (MAJOR.MINOR.PATCH) with creative names:
- **0.1.x** - "Arena Prototype" - Wave-based combat foundation
- **0.2.x** - "Room Cards" - Dungeon room system
- **0.3.x** - "The Awakening" - Advanced AI and themed rooms
- **0.4.x** - "The Cookbook" (Planned) - Skill discovery system
- **0.5.x** - "The Wardrobe" (Planned) - Equipment system
- **1.0.0** - "The Show Must Go On" - Full narrative campaign

[0.3.0]: https://github.com/yourusername/dcc-browser/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/yourusername/dcc-browser/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/yourusername/dcc-browser/releases/tag/v0.1.0
