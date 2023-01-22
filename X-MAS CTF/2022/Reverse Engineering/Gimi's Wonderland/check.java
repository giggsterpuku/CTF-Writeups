function to_bits(world, x, mode)
{
    var offset = 0;
    if (mode != 0)
    {
        offset = 2;
    }
    
    else
    {
        var tempdata = world.tempdata;
        var old_rkey = tempdata.get("rkey");
        tempdata.put("rkey", (x + old_rkey) & 0xFF);
        //print("Setting rkey " + ((x + old_rkey) & 0xFF));
    }
    
    for (var i = 0; i < 8; i++)
    {
        if (x & (1<<i))
        {
            world.setBlock(-291 + 4 * i + offset, 4, 629, "minecraft:redstone_block", 0);
        }
        else
        {
            world.setBlock(-291 + 4 * i + offset, 4, 629, "minecraft:wool", 14);
        }
    }
}

function from_bits(world)
{
    var xstart = -311;
    var tempdata = world.tempdata;
    var dict = {
    36: 'A',
    206: 'C',
    236: 'G',
    246: 'T'
    }
    
    if (tempdata.has("encflag"))
    {
        for(var i = 0; i < 4; i++)
        {
            var num = 0;
            for(var j = 0; j < 7; j++)
            {
                var x = xstart + 20 * i + 2 * j;
                var bl = world.getBlock(x, 4, 691).getName();
                if(bl == "minecraft:lit_redstone_lamp")
                {
                    num = num + 1;
                }
                num = num << 1;
            }
            tempdata.put("encflag", tempdata.get("encflag") + dict[num]);
        }
    }
    
    else
    {
        tempdata.put("encflag", "");
    }
}
function tick(event)
{
    var world = event.npc.getWorld();
    var tempdata = world.tempdata;
    
    if(((world.getTime() / 10) >> 0 )% 5 != 0)
    {
        return;
    }
    
    if (tempdata.has("flag"))
    {
        from_bits(world);
        var flag = tempdata.get("flag");
        if (flag.length == 0)
        {
            event.npc.say("Your champion gene is: " + tempdata.get("encflag"));
            if(tempdata.get("encflag") != "GACGCCTGACCCTTATATGGCGTATCCTTGAGCGGCCCCTAAGATCCCTCAGGGGTTTACGCGGAGACCTCTCAAAGGGTGGTGGCCCCTCAGCGAAGATCGAGTGGCAGCTGTCATGACGATTCATAGGATCCAGACTAGGCCATGA")
            {
                event.npc.say("Unfortunately, that's not what i'm looking for!");
            }
            else
            {
                event.npc.say("Thanks, you found it!");
            }
            
            print(tempdata.get("encflag"));
            tempdata.remove("flag");
            tempdata.remove("encflag");
        }
        
        else
        {
            var num = flag.charCodeAt(0);
            var chr = flag.substr(0, 1);
            to_bits(world, tempdata.get("rkey"), 1);
            to_bits(world, num, 0);
            event.npc.say("Processing " + chr);
            tempdata.put("flag", flag.substr(1));
        }
    }
}
