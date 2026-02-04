# Changelog

All notable changes to Dungeon Crawler Carl: The Browser Incident will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0] - 2026-02-03 - "The Iron Tangle"

### Added
- **Katia NPC**: Rival crawler who appears randomly in combat rooms (30% chance) on Floor 3+
  - Can be interacted with (Press Space when nearby)
  - Provides random buffs: speed boost, healing, items, or tips
  - Fights alongside player when enemies are present
  - Throws knives at enemies from range
- **6 New Complex Room Templates**:
  - Desecrated Cathedral - Large religious room with altar, side chapels, and pews
  - Chasm Bridge - Narrow bridge over deadly gap with platforms on each side
  - Maze of Madness - Complex labyrinth with many dead ends and tight corridors
  - Arena of Peril - Trapped arena with spike pits and corner platforms
  - Vertical Shaft - Tall narrow room with horizontal platforms
  - Collapsed Tunnel - Rubble-filled winding path with support beams
- **6 New Enemy Types** (appear on progressively higher floors):
  - Wraith 🌫️ (Floor 5+) - Fades in/out (invisible phases), fast melee attacker
  - Golem 🗿 (Floor 6+) - Slow heavy tank with AOE ground pound attack
  - Imp 👿 (Floor 5+) - Teleports around player, ranged fire attacks
  - Necromancer 🧙 (Floor 6+) - Summons skeleton minions, dark magic ranged attacks
  - Drake 🐉 (Floor 7+) - Flying enemy that ignores walls, cone fire breath attack
  - Banshee 👰‍♀️ (Floor 7+) - Screams to stun player, phases through walls
- **Boss System Overhaul**:
  - Boss encounters on EVERY floor (previously only floors 3, 6, 9)
  - Mini-bosses on floors 1, 2, 4, 5, 7, 8 (elite enemies or multiple tough foes)
  - Major bosses on floors 3, 6, 9 with elite guard spawns
  - Boss room variety: Arena, Throne Room, Cathedral, Arena of Peril (randomly selected)
  - Early floor "Challenge Rooms" with multiple enemies

### Changed
- Total enemy types expanded from 13 to 19
- Total room templates expanded from 17 to 23
- All 6 new complex rooms added to combat room rotation pool
- Progressive enemy unlock system: new enemies appear on higher floors (5-7)
- Enemy variety scales with floor depth for increased difficulty curve
- Boss difficulty scales with floor number

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
