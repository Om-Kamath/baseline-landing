import AppKit
let width = 1200, height = 630
let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: width, pixelsHigh: height, bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
NSColor(red: 250/255, green: 248/255, blue: 243/255, alpha: 1).setFill()
NSRect(x: 0,y: 0,width: width,height: height).fill()
func draw(_ str: String,_ x: CGFloat,_ y: CGFloat,_ size: CGFloat,_ color: NSColor,_ weight: NSFont.Weight = .regular) { (str as NSString).draw(at: NSPoint(x:x,y:y),withAttributes:[.font:NSFont.systemFont(ofSize:size,weight:weight),.foregroundColor:color]) }
let ink = NSColor(calibratedWhite: 0.067, alpha: 1)
let purple = NSColor(red: 0.62,green: 0.51,blue: 0.81,alpha: 1)
draw("YOUR HEALTH. YOUR NORMAL.",80,540,15,ink,.medium)
draw("baseline",65,260,214,ink,.black)
purple.setFill(); NSBezierPath(ovalIn: NSRect(x:950,y:307,width:39,height:39)).fill()
draw("Know how recovered you really are.",80,180,38,ink,.medium)
draw("Personal recovery & energy scores from Apple Health.",80,130,22,NSColor.darkGray)
draw("FREE & OPEN SOURCE  ·  PRIVATE BY DESIGN",80,55,13,ink,.medium)
purple.setStroke(); let circle=NSBezierPath(ovalIn:NSRect(x:1040,y:460,width:65,height:65));circle.lineWidth=2;circle.stroke()
let gold=NSColor(red:0.93,green:0.77,blue:0.25,alpha:1)
draw("✦",1060,205,100,gold)
NSGraphicsContext.restoreGraphicsState()
try rep.representation(using:.png,properties:[:])!.write(to: URL(fileURLWithPath:CommandLine.arguments[1]))
