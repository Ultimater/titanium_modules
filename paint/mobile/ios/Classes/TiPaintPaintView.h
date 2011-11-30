/**
 * Titanium Paint Module
 *
 * Appcelerator Titanium is Copyright (c) 2009-2010 by Appcelerator, Inc.
 * and licensed under the Apache Public License (version 2)
 */
#import "TiUIView.h"
#import "TiPaintModule.h"

@interface TiPaintPaintView : TiUIView {
@private
	UIImageView *drawImage;
	CGFloat strokeWidth;
	CGFloat strokeAlpha;
	CGColorRef strokeColor;
    int drawMode;
	bool erase;
}

@end
