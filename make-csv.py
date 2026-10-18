import csv

csv_data = [
    ["Category", "Item Name", "Key Specifications / Notes", "Qty", "Est. Cost"],
    ["Surfaces & Tile", "Floor Tiles", "Slip-resistant matte porcelain. Calculate floor sq. ft. plus a 10% waste buffer.", "", ""],
    ["Surfaces & Tile", "Wall Tiles", "Clean ceramic or porcelain for the main wall field.", "", ""],
    ["Surfaces & Tile", "Wall Decoration Tiles", "Accent or mosaic tiles for a feature layout backdrop.", "", ""],
    ["Surfaces & Tile", "Tub/Shower Tiles", "Waterproof vertical tiles surrounding the bathing area.", "", ""],
    ["Wet Area & Fixtures", "Bathtubs (Left-Drain Alcove)", "KOHLER Underscore 60\" x 30\" Left-Hand Drain Alcove Soaking Tub (White, K-20201-LA-0)", "1", "~$1096"],
    ["Wet Area & Fixtures", "Tub Drain & Overflow", "KOHLER Clearflo Slotted Overflow Bath Drain (K-7271 or K-7272)", "1", "~$150-$250"],
    ["Wet Area & Fixtures", "Tub/Shower Faucets with Head & Spout", "Pressure-balancing shower valve trim kit, showerhead arm, and down-spout.", "1", ""],
    ["Wet Area & Fixtures", "Shower Shelving / Niche", "Prefabricated leak-proof recessed wall box (ready-for-tile or stainless steel).", "1", ""],
    ["Wet Area & Fixtures", "Glass Partition for Tub/Shower", "Fixed or hinged frameless glass splash panel. Clean alternative to a curtain.", "1", ""],
    ["Core Fixtures", "Toilet", "Sleek skirted floor-mount or space-saving wall-hung toilet.", "1", ""],
    ["Core Fixtures", "Floating Sink / Vanity", "Wall-mounted vanity cabinet with an integrated quartz or ceramic top.", "1", ""],
    ["Mechanical/Electrical", "Lighted Vanity Mirror / Medicine Cabinet", "DEERVALLEY or ExBrite Recessed/Surface LED Medicine Cabinet with defogger and internal outlets.", "1", ""],
    ["Mechanical/Electrical", "Exhaust Fan / Light Combo", "Ultra-quiet ceiling fan. Verify CFM rating matches your room size.", "1", ""],
    ["Mechanical/Electrical", "Ambient Recessed Ceiling Lights", "Dimmable 3000K/4000K 90+ CRI LED recessed downlights for overall room illumination.", "2-4", ""],
    ["Mechanical/Electrical", "LED Wall Dimmer Switches", "Electronic dimmer switches to control vanity and ceiling lighting independently.", "2", ""],
    ["Accessories", "Tile Toilet Paper Holder", "Recessed ceramic or porcelain accessory built directly into the wet tile field.", "1", ""],
    ["Building Materials", "Grout", "High-performance, anti-mold stain-resistant polymer or epoxy grout.", "", ""],
    ["Building Materials", "Paint", "Premium mildew-resistant, anti-microbial bathroom paint (Satin/Semi-Gloss).", "1", ""],
    ["Hidden Tub Support", "Structolite / Mortar Mix", "Standard mortar mix bags to place underneath the tub shell to prevent flexing.", "2", ""],
    ["Hidden Tub Support", "2x4 Lumber Studs", "For building the level support ledge along the back wall under the tub lip.", "2", ""],
    ["Hidden Tub Support", "Integral 3-Side Tile Flange", "Watertight tile bead kit to seal the tub shell completely against the drywall.", "1", ""],
    ["Vanity Support", "HD Floating Vanity Brackets", "Heavy-duty steel support brackets bolted directly into studs to support weight.", "2", ""],
    ["Wall & Tile Prep", "1/2\" Cement Backer Board", "Mold-resistant backing boards for all tile areas (e.g., USG Durock).", "", ""],
    ["Wall & Tile Prep", "Under-Tile Waterproofing Kit", "Waterproofing membrane sheets/bands (e.g., Schluter-KERDI system).", "1", ""],
    ["Plumbing & Seals", "Rough-In Plumbing Valves", "Internal brass mixing valves behind the wall. *Must match your faucet brand.*", "1", ""],
    ["Plumbing & Seals", "Supply Shut-Off Valves", "Fresh 1/2\" quarter-turn compression valves for sink and toilet lines.", "3", ""],
    ["Plumbing & Seals", "Deep-Seal P-Trap Tube", "Fresh PVC or brass P-trap tube assembly to ensure tight, clean plumbing lines.", "1", ""],
    ["Plumbing & Seals", "100% Silicone Caulk", "Color-matched caulk for internal corner joints and tub-to-tile edges.", "2", ""]
]

print("Table Preview:")
for row in csv_data[:16]:
    print(f"| {' | '.join(row)} |")
