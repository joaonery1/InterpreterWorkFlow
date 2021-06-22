
/*********************************************************************
***                                                                 ***
***  Source code generated by glsl2cpp.pl                           ***
***                                                                 ***
***  Please do not edit                                             ***
***                                                                 ***
*********************************************************************/
#include "vglImage.h"

void shader_15_1(VglImage* src, VglImage* dst);

/** Convert grayscale image to RGB

  */
void vgl1to3Channels(VglImage* src, VglImage* dst);

/** Inverts 3d image.

    As the wrappers are implemented currently, the shader will invert only the first layer of the 3d image.

  */
void vgl3dNot(VglImage* src, VglImage* dst);

/** Absolute difference between two images.

  */
void vglAbsDiff(VglImage* src0, VglImage* src1, VglImage* dst);

/** Logical AND between two images

  */
void vglAnd(VglImage* src0, VglImage* src1, VglImage* dst);

/** Initialize image to be used in baricenter calculation. The initialization is done by storing the values (1, x, y) in each output pixel so that the summation over th whole image gives the three moments of the image.

    R =                    f(x, y) 

    G =                x * f(x, y) 

    B =                y * f(x, y) 

  */
void vglBaricenterInit(VglImage* src, VglImage* dst);

/** vglBlurSq3

    Blur image by 3x3 square structuring element.

  */
void vglBlurSq3(VglImage* src, VglImage* dst);

/** Clear image with given color.

  */
void vglClear2(VglImage* src_dst, float r, float g, float b, float a= 0.0);

/** Changes contrast of image by given factor.

  */
void vglContrast(VglImage* src, VglImage* dst, float factor);

/** Shows coordinates of pixels as colors. Red is horizontal and green is vertical. Coordinates and colors are defined by OpenGL, that is, between 0 and 1.

  */
void vglCoordToColor(VglImage* dst);

/** Direct copy from src to dst.

  */
void vglCopy(VglImage* src, VglImage* dst);

/** Crossing number is defined as the number of ocurrences of the pattern 01
in the neihborhood of a pixel.

    Neighborhood of pixel P is indexed as follows:

\f$
\begin{array}{ccc}

    P3   &  P2   &  P1      \\ 
    P4   &  P    &  P0/8    \\
    P5   &  P6   &  P7

\end{array}
\f$


    References:

    M. Couprie, Note on fifteen 2D parallel thinning algorithms, 2006

    T. M. Bernard and A. Manzanera, Improved low complexity fully parallel
        thinning algorithms, 1999

  */
void vglCrossingNumber(VglImage* src, VglImage* dst);

/** Deletes corner from skeleton.

    Receive as input the image with the skeleton to be thinned. Receives 
    also the step. must be called once with step 1 and once with step 2.

    Neighborhood pixels is indexed as follows:

\f$
\begin{array}{ccc}

    P3  &  P2  &  P1      \\
    P4  &  P8  &  P0      \\
    P5  &  P6  &  P7

\end{array}
\f$


    Pixels deleted are the ones that mach the pattern and its rotations 
    by 90deg.

\f$
\begin{array}{ccc}

    0  &  0  &  x      \\
    0  &  1  &  1      \\
    x  &  1  &  0

\end{array}
\f$

    References:

    M. Couprie, Note on fifteen 2D parallel thinning algorithms, 2006

    T. M. Bernard and A. Manzanera, Improved low complexity fully parallel
        thinning algorithms, 1999

  */
void vglDeleteSkeletonCorners(VglImage* src, VglImage* dst, int step);

/** Deletes warts from skeleton. Receive as input the image with the skeleton to be thinned. Neighborhood pixels are indexed as follows:

\f$
\begin{array}{ccc}

    P3  &  P2  &  P1      \\
    P4  &  P   &  P0/8    \\
    P5  &  P6  &  P7

\end{array}
\f$

    Pixels deleted are the ones that mach the pattern and its rotations 
    by 45deg.

\f$
\begin{array}{ccc}

    1  &  0  &  0    \\
    1  &  1  &  0    \\
    1  &  0  &  0

\end{array}
\f$

    That is the same as delete the pixels with crossing number = 1 and 
neighbor number = 3

    References:

    Ke Liu et al., Identification of fork points on the skeletons
        of handwritten chinese characters

  */
void vglDeleteSkeletonWarts(VglImage* src, VglImage* dst);

/** Deletes warts from skeleton. Receive as input the image with the skeleton to be thinned. Neighborhood pixels are indexed as follows:

    P3 P2 P1

    P4 P  P0/8

    P5 P6 P7

    Pixels deleted are the ones that mach the pattern and its rotations 
    by 45deg.

    1 0 0
    1 1 0
    1 0 0

    1 1 0
    1 1 0
    1 0 0

    1 1 0
    1 1 0
    1 1 0

    1 1 1
    1 1 0
    1 1 0

    1 1 1
    1 1 0
    1 1 1


    That is the same as delete the pixels with crossing number = 1 and 
neighbor number >=3

    References:

    Ke Liu et al., Identification of fork points on the skeletons
        of handwritten chinese characters

  */
void vglDeleteSkeletonWarts2(VglImage* src, VglImage* dst);

/** Image src0 minus src1.

  */
void vglDiff(VglImage* src0, VglImage* src1, VglImage* dst);

/** Dilation of image by 3x3 cross structuring element.

  */
void vglDilateCross3(VglImage* src, VglImage* dst);

/** Dilation of image by 3x3 square structuring element.

  */
void vglDilateSq3(VglImage* src, VglImage* dst);

/** Erosion of image by 3x3 cross structuring element.

  */
void vglErodeCross3(VglImage* src, VglImage* dst);

/** Erosion of image by horizontal line with 3 pixels.

  */
void vglErodeHL3(VglImage* src, VglImage* dst);

/** Erosion of image by horizontal line with 5 pixels.

  */
void vglErodeHL5(VglImage* src, VglImage* dst);

/** Erosion of image by horizontal line with 7 pixels.

  */
void vglErodeHL7(VglImage* src, VglImage* dst);

/** Erosion of image by 3x3 square structuring element.

  */
void vglErodeSq3(VglImage* src, VglImage* dst);

/** Erosion of image by 3x3 square structuring element. Uses an offset array with 9 elements. Slower than vglErodeSq3.

  */
void vglErodeSq3off(VglImage* src, VglImage* dst);

/** Erosion of image by 5x5 square structuring element.

  */
void vglErodeSq5(VglImage* src, VglImage* dst);

/** Erosion of image by 3x3 square structuring element. Uses an offset array with 25 elements. Slower than vglErodeSq5.

  */
void vglErodeSq5off(VglImage* src, VglImage* dst);

/** Erosion of image by 7x7 square structuring element.

  */
void vglErodeSq7(VglImage* src, VglImage* dst);

/** Erosion of image by square structuring element. The parameter "side" is the dimension of the square side in pixels.

  */
void vglErodeSqSide(VglImage* src, VglImage* dst, int side);

/** Erosion of image by vertical line with 3 pixels.

  */
void vglErodeVL3(VglImage* src, VglImage* dst);

/** Erosion of image by vertical line with 5 pixels.

  */
void vglErodeVL5(VglImage* src, VglImage* dst);

/** Erosion of image by vertical line with 7 pixels.

  */
void vglErodeVL7(VglImage* src, VglImage* dst);

/** Feature Points are defined as function of the crossing number
and number of neighbors of a pixel. 

The number of neighbors is indicated as Nb. Crossing number is defined as

Nc = number of occurrences of the pattern 01 in the neighborhood of P

    Neighborhood pixels are indexed as follows:

    P3 P2 P1

    P4 P  P0

    P5 P6 P7


    All the ending points are feature points. Are defined as
Se = { P | Nc(P) = 1 }


    Feature points type 1, denoted as S1, are defined as
S1 = { P | Nc(P) >= 3}

    Feature points type 2, denoted as S2, are defined as
S1 = { P | Nb(P) >= 3}

    Feature points type 3, denoted as S3, are defined as
S3 = { P | Nc(P) >= 3 or Nb(P) >= 4 }


    References:

    Ke Liu et al., Identification of fork points on the skeletons
        of handwritten chinese characters

  */
void vglFeaturePoints(VglImage* src, VglImage* dst, int type);

/** Blurs image by 3x3 square gaussian structuring element.

  */
void vglGaussianBlurSq3(VglImage* src, VglImage* dst);

/** Convert image to grayscale by calculating the scalar product of (r, g, b) and (.2125, .7154, .0721).

  */
void vglGray(VglImage* src, VglImage* dst);

/** Flip image horizontally i.e. left becomes right.

    Image flip done by shader.
  */
void vglHorizontalFlip(VglImage* src, VglImage* dst);

/** vglInOut

    Test and model for IN_OUT semantics

  */
void vglInOut(VglImage* src, VglImage* dst);

/** Calculate Julia set

  */
void vglJulia(VglImage* dst, float ox= 0.0, float oy= 0.0, float half_win= 1.0, float c_real= -1.36, float c_imag= .11);

/** Laplacian of image by 3x3 square structuring element.

  */
void vglLaplaceSq3(VglImage* src, VglImage* dst);

/** Calculate Mandelbrot set

  */
void vglMandel(VglImage* dst, float ox= 0.0, float oy= 0.0, float half_win= 1.0);

/** Get specified level of detail.

  */
void vglMipmap(VglImage* src, VglImage* dst, float lod);

/** Multiply image by scalar.

  */
void vglMulScalar(VglImage* src, VglImage* dst, float factor);

/** VglAdd

    Sum of two images.

  */
void vglMultiInput(VglImage* src0, VglImage* src1, VglImage* dst, float weight= .5);

/** vglGray

    Convert image to grayscale

  */
void vglMultiOutput(VglImage* src, VglImage* dst, VglImage* dst1);

/** Add gaussian noise to image

  */
void vglNoise(VglImage* src, VglImage* dst);

/** Inverts image.

  */
void vglNot(VglImage* src, VglImage* dst);

/** Logical OR between two images

  */
void vglOr(VglImage* src0, VglImage* src1, VglImage* dst);

/** Rescales corners of image to given corners

  */
void vglRescale(VglImage* src, VglImage* dst, float x0, float y0, float x1, float y1);

/** Converts image RGB to BGR color space

  */
void vglRgbToBgr(VglImage* src, VglImage* dst);

/** Converts image RGB to HSL color space

  */
void vglRgbToHsl(VglImage* src, VglImage* dst);

/** Converts image RGB to HSV color space

  */
void vglRgbToHsv(VglImage* src, VglImage* dst);

/** Converts image RGB to XYZ color space.

  */
void vglRgbToXyz(VglImage* src, VglImage* dst);

/** Roberts gradient of image

  */
void vglRobertsGradient(VglImage* src, VglImage* dst);

/** Stores in output pixel the sum of 4 adjacent pixels of the input
    image. 
    The width and height of the output image must be half of the input image.

  */
void vglSelfSum22(VglImage* src, VglImage* dst);

/** Stores in output pixel the sum of 3 adjacent pixels of the input
    image. 
    The height of the output image must be 1/3th of the input image.

  */
void vglSelfSum3v(VglImage* src, VglImage* dst);

/** Stores in output pixel the sum of 4 adjacent pixels of the input
    image. 
    The width of the output image must be 1/4th of the input image.

  */
void vglSelfSum4h(VglImage* src, VglImage* dst);

/** Stores in output pixel the sum of 5 adjacent pixels of the input
    image. 
    The width of the output image must be 1/5th of the input image.

  */
void vglSelfSum5h(VglImage* src, VglImage* dst);

/** Stores in output pixel the sum of 5 adjacent pixels of the input
    image. 
    The height of the output image must be 1/5th of the input image.

  */
void vglSelfSum5v(VglImage* src, VglImage* dst);

/** Sharpens image using 3x3 square window.

  */
void vglSharpenSq3(VglImage* src, VglImage* dst);

/** Sobel gradient of image

  */
void vglSobelGradient(VglImage* src, VglImage* dst);

/** Sobel edge filtering in X direction.

  */
void vglSobelXSq3(VglImage* src, VglImage* dst);

/** Sobel edge filtering in Y direction.

  */
void vglSobelYSq3(VglImage* src, VglImage* dst);

/** Sum of two images.

  */
void vglSum(VglImage* src0, VglImage* src1, VglImage* dst);

/** Weighted sum of two images. The first image is multiplied by weight, and the second, by 1 - weight. Default weight is 0.5.

  */
void vglSumWeighted(VglImage* src0, VglImage* src1, VglImage* dst, float weight= .5);

/** Convert image from RGB to BGR and vice versa.

  */
void vglSwapRGB(VglImage* src, VglImage* dst);

/** Test and model for IN_OUT semantics

  */
void vglTestInOut(VglImage* src_dst, float r, float g, float b, float a= 0.0);

/** Test and model for IN_OUT semantics, with double output.

  */
void vglTestInOut2(VglImage* src_dst, VglImage* dst);

/** Test and model for multiple input functions.

  */
void vglTestMultiInput(VglImage* src0, VglImage* src1, VglImage* dst, float weight= .5);

/** Test and model for multiple output functions.

  */
void vglTestMultiOutput(VglImage* src, VglImage* dst, VglImage* dst1);

/** vglDilate

    Dilation of image by 3x3 square structuring element.

  */
void vglTeste(VglImage* src, VglImage* dst);

/** Return one step of thinning. 
    Algorithm by Bernard and Manzanera 1999.
    Receive as input the image to be thinned and its erosion by a elementary 
cross structuring element.
    Neighborhood pixels are indexed as follows:

\f$
\begin{array}{ccc}

    P3  &  P2  &  P1    \\
    P4  &  P8  &  P0    \\
    P5  &  P6  &  P7

\end{array}
\f$

    References:

    M. Couprie, Note on fifteen 2D parallel thinning algorithms, 2006

    T. M. Bernard and A. Manzanera, Improved low complexity fully parallel
        thinning algorithms, 1999

  */
void vglThinBernardAux(VglImage* src, VglImage* eroded, VglImage* dst);

/** Return one step of thinning.
    Algorithm by Chin, Wan Stover and Iverson, 1987.
    Receive as input the image to be thinned, buffer image and number 
    of times to iterate.
    Neighborhood pixels are indexed as follows:

\f$ 
\begin{array}{ccccc}

    x   & x   & P10 & x   & x    \\

    x   & P3  & P2  & P1  & x    \\

    P11 & P4  & P0  & P8  & P9   \\

    x   & P5  & P6  & P7  & x    \\

    x   & x   & P12 & x   & x

\end{array}
\f$ 

    References:

    M. Couprie, Note on fifteen 2D parallel thinning algorithms, 2006

    R. T. Chin et al., A one-pass thinning algorithm and its parallel 
        implementation, 1987
  */
void vglThinChinAux(VglImage* src, VglImage* dst);

/** Threshold of image. If value is greater than threshold, output is top,
    else, output is 0. Default top value is 1.

  */
void vglThresh(VglImage* src, VglImage* dst, float thresh, float top= 1.0);

/** Threshold of image. If value is equal to level, output is top,
    else, output is 0. Default top value is 1.  
    Use after some Distance Transform to get a single distance level set.

  */
void vglThreshLevelSet(VglImage* src, VglImage* dst, float thresh, float top= 1.0);

/** Flip image vertically i.e. top becomes bottom.

    Image flip done by shader.
  */
void vglVerticalFlip(VglImage* src, VglImage* dst);

/** Finds edge by using a White-Rohrer mask.

  */
void vglWhiteRohrerEdge(VglImage* src, VglImage* dst, float radius);

/** Stores sobel edge filtering in X direction in red channel
    grayscale in y and sobel edge filtering in Y direction in green channel

  */
void vglXGY(VglImage* src, VglImage* dst);

/** Zoom image by factor.

  */
void vglZoom(VglImage* src, VglImage* dst, float factor);

