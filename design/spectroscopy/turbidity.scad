$fn=100;
/*
Block LED holder suitable for 5 mm LED.  Contains a stop for preventing LED from being inserted too far and is curved for a 40 degree arc.

210730- printed at 0.35 layer height, h1 is a tad small which prevents led from being inserted completely but provides some stability as it "snaps" into place.

Scaling 1.05 results in a very tight (one way) fit.  1.08 seems to work, as does a cell size of 7.6

Fixed source port to base since the sliders are too close together.

*/
r = 14.62; // Radius of device
w = 10; // length of chord (deprecated?)
h = 0.88; // height of arc ( deprecated?)
d1 = 6.8; // diameter of LED lip 
d2 = 5.4; // diameter of LED bulb
h1 = 5; // Arbitrary height for LED holder
h2 = 7.8; // height of LED bulb
hd = 1; // height for transition from d1 to d2
ht = h1 + h2 + hd + h;
zt = 10; // how tall the device is
xt = 12; // maximum width of LED holder
a = 112.5; // 90 + doc/2 where doc is degree of curvature
tol = 1; // Arbitrary for cleaner rendering
lipx = 1; // size of LED holder lip in x dimension
lipy = 2; // size of LED holder lip in y dimension
cell = 7.6; // sample holder diameter
sc = 1.08; // Empirical scaling to fit LED holder to base.

// Hole in the LED holder that securely holds the LED in place.  Unfortunately, a one size fits all approach isn't going to work, as different LEDs have slightly different lip diameters.
module cutout() {
    // Three cylinders on top of one another.  Larger diameter (d1) allows the lip of LED through.  It's height is arbitrary.  Transition from d1 to d2 probably only needed for rotated printing.  d2 and h2 are the height and diameter of the bulb.
    translate([0,0,zt/2])rotate(90,[1,0,0])translate([0,0,-ht/2])union(){
        translate([0,0,-tol])cylinder(d=d1,h=h1+tol);
        translate([0,0,h1])cylinder(d1=d1,d2=d2,h=hd);
        translate([0,0,h1+hd])cylinder(d=d2,h=h2+tol);
    }
}

// the LED holder consists of a solid block with a lip formed by subtracting two 
module block(){
    
    linear_extrude(zt)
    // center the final object
    translate([0,-r*sin(a)-ht/2])
    // disk with block protruding from it
    union(){
        difference(){
            translate([lipx-xt/2,r*sin(a)])square([xt-2*lipx,ht]);
            circle(r=r);
        }
    //Lip
    intersection(){
            translate([-xt/2,0])square([xt,3*ht]);
            difference(){
                circle(r=r+lipy);
                circle(r=r);
            }
        }
    }
}


module ledholder(){
    difference(){
        block();
        cutout();
    }    
}


// base contains a sample holder with diameter `cell` and radius `r`.  One LED holder is permanently fixed to the base as the source.  Three lips are extracted from the base at 180, 90 and 45 degres to allow for absorption and scattering measurements.
module base(){
    difference(){
        // Create circular base with one permanently fixed  LED holder.
        union(){
            linear_extrude(zt) circle(r=r+lipy+1);
            rotate(180,[0,0,1])translate([0,r*sin(a)+ht/2,0])ledholder();
        }
        union(){
            // Carve out sample holder 
            translate([0,0,-tol])cylinder(r=cell,h=zt+2*tol);
            // Carve out spaces for the LED holder lips
            for (i = [0,  90, 225]){
                rotate(i,[0,0,1])
                translate([0,r*sin(a)+ht/2,-tol])
                scale([sc,sc,1.2])block();
            }
            // Carve out holes for light
            for(i = [0,-90,180,45]){
                rotate(i,[0,0,1])
                translate([0,0,zt/2])
                rotate(90,[1,0,0])cylinder(d=3,h=2*r);
            }
        }
    }
}


// LED holder will need some way to secure the LED.  Make a compression fit cap.
module cap(){
    difference(){
        union(){
            // Cap top and hexagonal plug wtih same dimensions as the LED holder
            cylinder(d=1.2*d1,h=0.9);
            translate([0,0,0.9])
            cylinder(d=d1,h=0.95*h1,$fn=6);
        }
        for(i=[-1.25,1.25])
            // Carve out space for the LED legs
            translate([i,0,-tol])cylinder(d=1,h=2*h1,$fn=6);
    }
}
        


*cap();
*translate([0,ht+7,0])ledholder();
*base();
block();


