# Dungeon Crawler Carl: The Browser Incident

**Version 0.4.0 - "The Iron Tangle"**

A browser-based dungeon crawler game inspired by the web novel series "Dungeon Crawler Carl" by Matt Dinniman. This game is built using HTML5 Canvas, CSS, and vanilla JavaScript.

> 🎮 **Latest Update**: Katia NPC rival crawler, 6 complex room templates, and 6 new high-tier enemies!

## How to Run

1. Open `DCC.html` in a modern web browser (Chrome, Firefox, Safari, Edge).
2. Alternatively, serve it via a local HTTP server to avoid CORS issues:
   ```bash
   python -m http.server 8000
   ```
   Then navigate to `http://localhost:8000/DCC.html`.

## Game Overview

Players control Carl and his cat Donut as they navigate through procedurally generated dungeon floors, fighting monsters, collecting loot, and clearing rooms to progress deeper. The game features:

- **Procedural room-based dungeons** with 23 unique layouts
- **19 enemy types** with unique AI behaviors and mechanics
- **Proximity-based AI** - enemies sleep until you get close
- **Katia NPC** - Rival crawler who appears randomly, provides buffs and fights alongside you
- **Themed rooms** - Cathedral, Chasm Bridge, Labyrinth, Treasure Vault, Crypt, Throne Room, Library, Prison
- **Advanced enemy mechanics** - slimes split, skeletons revive, ghosts phase through walls, necromancers summon minions
- Real-time tactical combat with positioning and cover
- Inventory system with bombs, potions, traps, and special items
- Live chat simulation with viewer interactions
- Achievement system with unlockables
- Boss fights and safe rooms (The Prancing Princess pub)
- Room modifiers (Darkness, Flood, Audience Favorite)

## Code Structure

The entire game is contained in a single HTML file (`DCC.html`) with embedded CSS and JavaScript.

### HTML Structure

- **Head**: Meta tags, title, and Google Fonts imports (VT323 for monospace text, Black Ops One for bold elements)
- **Body**: 
  - `#game-container`: Main container holding the canvas and UI overlays
  - `#gameCanvas`: HTML5 Canvas element for rendering the game world
  - `#ui-layer`: Overlay containing HUD, inventory, chat, and other UI elements
  - `#crt-overlay`: Retro TV scanline effect

### CSS Styles

The CSS is organized into sections for different UI components:

- **Body and Canvas**: Basic layout and pixelated rendering
- **HUD**: Health bar, XP bar, score displays
- **Timer**: Floor collapse countdown
- **Hype Meter**: Viewer engagement indicator
- **Combo Display**: Multi-kill streak notifications
- **Boss Bar**: Health bar for boss enemies
- **TV Overlay**: Simulated live stream chat
- **Inventory**: Item slots with keyboard shortcuts
- **System Log**: Game messages and notifications
- **Announcement Banner**: Major event notifications
- **Party Banter Overlay**: Character dialogue bubbles

### JavaScript Code

The JavaScript code is divided into logical sections:

#### Constants and Data Structures

- **COLORS**: Color palette for the game
- **ITEMS**: Definitions for usable items (potions, bombs, etc.)
- **SPRITES**: Emoji representations for game entities
- **SPLASH_QUOTES**: Flavor text for different game events
- **SYSTEM_QUOTES**: System messages for various events
- **UPGRADES**: Stat upgrade options
- **MORDECAI_TIPS**: Tutorial hints from the narrator
- **PARTY_CHAT**: Dialogue between Carl and Donut
- **LOOT_TABLE**: Possible loot drops with rarities

#### Classes

- **Vector2**: 2D vector class for positions, velocities, and calculations
  - Methods: add(), sub(), mag(), normalize(), scale(), dist()
- **Entity**: Base class for all game entities (players, enemies, items)
  - Properties: position, size, icon, state flags
  - Methods: update(), draw()
- **Particle**: Visual effects like blood splatters or explosions
  - Properties: position, velocity, color, size, lifetime
  - Methods: update(), draw()

#### Game Systems

- **Audio System**: Web Audio API for sound effects and speech synthesis
- **Achievement System**: Tracks player accomplishments
- **Chat Systems**: Simulates live stream chat with random messages
- **UI Management**: Updates HUD elements, overlays, and screens

#### Game Loop

The main game loop handles:
- Input processing (keyboard and touch)
- Entity updates and physics
- Collision detection
- Rendering
- UI updates

#### Key Functions

- `initGame()`: Initializes game state and starts the first floor
- `update(dt)`: Main update loop called each frame
- `draw()`: Renders the game world and UI
- `handleInput()`: Processes keyboard and touch input
- `spawnEnemy()`: Creates new enemy entities
- `checkCollisions()`: Detects and resolves entity interactions
- `showAnnouncement()`: Displays major game events
- `logMessage()`: Adds messages to the system log

## Controls

- **WASD** or **Arrow Keys**: Move Carl
- **Mouse/Touch**: Aim and attack (auto-targets nearest enemy)
- **1-3**: Use inventory items
- **Space**: Interact with objects
- **Touch Joystick**: Mobile controls for movement

## Features

- **Procedural Generation**: Random dungeon layouts and enemy spawns
- **Real-time Combat**: Fast-paced action with combo systems
- **Item System**: Strategic use of bombs, potions, and traps
- **Live Simulation**: Chat feed and hype meter create stream-like atmosphere
- **Achievements**: Unlockable accomplishments for replayability
- **Mobile Support**: Touch controls and responsive design
- **Retro Aesthetics**: CRT monitor effects and pixel art style

## Browser Compatibility

Requires a modern browser with support for:
- HTML5 Canvas
- ES6 JavaScript features
- Web Audio API (optional, falls back gracefully)
- CSS Grid and Flexbox

## Development Notes

- All code is in a single file for simplicity
- Uses emoji sprites for cross-platform compatibility
- Implements custom physics and collision detection
- Audio is generated procedurally using oscillators
- Touch controls use pointer events for broad device support

## Credits

Inspired by "Dungeon Crawler Carl" by Matt Dinniman.
Built with vanilla web technologies - no external libraries required.