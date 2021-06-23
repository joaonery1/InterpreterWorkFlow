
"""
    ************************************************************************
    ***                                                                  ***
    ***                Source code generated by cl2py.pl                 ***
    ***                                                                  ***
    ***                        Please do not edit                        ***
    ***                                                                  ***
    ************************************************************************
"""
#!/usr/bin/python3 python3

# OPENCL LIBRARY
import pyopencl as cl

# VGL LIBRARYS
import vgl_lib as vl

#TO WORK WITH MAIN
import numpy as np


"""
    /** Convolution of src image by mask. Result is stored in dst image.
    
    In some OpenCL versions, the next directive is required
    #pragma OPENCL EXTENSION cl_khr_3d_image_writes : enable

  */    
"""
def vglCl3dBlurSq3(img_input, img_output):

    vl.vglCheckContext(img_input, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglCl3dBlurSq3.cl", "vglCl3dBlurSq3")
    _kernel = _program.vglCl3dBlurSq3

    _kernel.set_arg(0, img_input.get_oclPtr())
    _kernel.set_arg(1, img_output.get_oclPtr())

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input.get_oclPtr().shape, None)

    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Convolution of src image by mask. Result is stored in dst image.

  */    
"""
def vglCl3dConvolution(img_input, img_output, convolution_window, window_size_x, window_size_y, window_size_z):

    vl.vglCheckContext(img_input, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())
    # EVALUATING IF convolution_window IS IN CORRECT TYPE
    try:
        mobj_convolution_window = cl.Buffer(vl.get_ocl().context, cl.mem_flags.READ_ONLY, convolution_window.nbytes)
        cl.enqueue_copy(vl.get_ocl().commandQueue, mobj_convolution_window, convolution_window.tobytes(), is_blocking=True)
        convolution_window = mobj_convolution_window
    except Exception as e:
        print("vglClConvolution: Error!! Impossible to convert convolution_window to cl.Buffer object.")
        print(str(e))
        exit()
    # EVALUATING IF window_size_x IS IN CORRECT TYPE
    if( not isinstance(window_size_x, np.uint32) ):
        print("vglClConvolution: Warning: window_size_x not np.uint32! Trying to convert...")
        try:
            window_size_x = np.uint32(window_size_x)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert window_size_x as a np.uint32 object.")
            print(str(e))
            exit()
    # EVALUATING IF window_size_y IS IN CORRECT TYPE
    if( not isinstance(window_size_y, np.uint32) ):
        print("vglClConvolution: Warning: window_size_y not np.uint32! Trying to convert...")
        try:
            window_size_y = np.uint32(window_size_y)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert window_size_y as a np.uint32 object.")
            print(str(e))
            exit()
    # EVALUATING IF window_size_z IS IN CORRECT TYPE
    if( not isinstance(window_size_z, np.uint32) ):
        print("vglClConvolution: Warning: window_size_z not np.uint32! Trying to convert...")
        try:
            window_size_z = np.uint32(window_size_z)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert window_size_z as a np.uint32 object.")
            print(str(e))
            exit()

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglCl3dConvolution.cl", "vglCl3dConvolution")
    _kernel = _program.vglCl3dConvolution

    _kernel.set_arg(0, img_input.get_oclPtr())
    _kernel.set_arg(1, img_output.get_oclPtr())
    _kernel.set_arg(2, mobj_convolution_window)
    _kernel.set_arg(3, window_size_x)
    _kernel.set_arg(4, window_size_y)
    _kernel.set_arg(5, window_size_z)

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input.get_oclPtr().shape, None)

    mobj_convolution_window = None
    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Direct copy from src to dst.

  */    
"""
def vglCl3dCopy(img_input, img_output):

    vl.vglCheckContext(img_input, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglCl3dCopy.cl", "vglCl3dCopy")
    _kernel = _program.vglCl3dCopy

    _kernel.set_arg(0, img_input.get_oclPtr())
    _kernel.set_arg(1, img_output.get_oclPtr())

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input.get_oclPtr().shape, None)

    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Erosion of src image by mask. Result is stored in dst image.

  */    
"""
def vglCl3dDilate(img_input, img_output, convolution_window, window_size_x, window_size_y, window_size_z):

    vl.vglCheckContext(img_input, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())
    # EVALUATING IF convolution_window IS IN CORRECT TYPE
    try:
        mobj_convolution_window = cl.Buffer(vl.get_ocl().context, cl.mem_flags.READ_ONLY, convolution_window.nbytes)
        cl.enqueue_copy(vl.get_ocl().commandQueue, mobj_convolution_window, convolution_window.tobytes(), is_blocking=True)
        convolution_window = mobj_convolution_window
    except Exception as e:
        print("vglClConvolution: Error!! Impossible to convert convolution_window to cl.Buffer object.")
        print(str(e))
        exit()
    # EVALUATING IF window_size_x IS IN CORRECT TYPE
    if( not isinstance(window_size_x, np.uint32) ):
        print("vglClConvolution: Warning: window_size_x not np.uint32! Trying to convert...")
        try:
            window_size_x = np.uint32(window_size_x)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert window_size_x as a np.uint32 object.")
            print(str(e))
            exit()
    # EVALUATING IF window_size_y IS IN CORRECT TYPE
    if( not isinstance(window_size_y, np.uint32) ):
        print("vglClConvolution: Warning: window_size_y not np.uint32! Trying to convert...")
        try:
            window_size_y = np.uint32(window_size_y)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert window_size_y as a np.uint32 object.")
            print(str(e))
            exit()
    # EVALUATING IF window_size_z IS IN CORRECT TYPE
    if( not isinstance(window_size_z, np.uint32) ):
        print("vglClConvolution: Warning: window_size_z not np.uint32! Trying to convert...")
        try:
            window_size_z = np.uint32(window_size_z)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert window_size_z as a np.uint32 object.")
            print(str(e))
            exit()

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglCl3dDilate.cl", "vglCl3dDilate")
    _kernel = _program.vglCl3dDilate

    _kernel.set_arg(0, img_input.get_oclPtr())
    _kernel.set_arg(1, img_output.get_oclPtr())
    _kernel.set_arg(2, mobj_convolution_window)
    _kernel.set_arg(3, window_size_x)
    _kernel.set_arg(4, window_size_y)
    _kernel.set_arg(5, window_size_z)

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input.get_oclPtr().shape, None)

    mobj_convolution_window = None
    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Erosion of src image by mask. Result is stored in dst image.

  */    
"""
def vglCl3dErode(img_input, img_output, convolution_window, window_size_x, window_size_y, window_size_z):

    vl.vglCheckContext(img_input, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())
    # EVALUATING IF convolution_window IS IN CORRECT TYPE
    try:
        mobj_convolution_window = cl.Buffer(vl.get_ocl().context, cl.mem_flags.READ_ONLY, convolution_window.nbytes)
        cl.enqueue_copy(vl.get_ocl().commandQueue, mobj_convolution_window, convolution_window.tobytes(), is_blocking=True)
        convolution_window = mobj_convolution_window
    except Exception as e:
        print("vglClConvolution: Error!! Impossible to convert convolution_window to cl.Buffer object.")
        print(str(e))
        exit()
    # EVALUATING IF window_size_x IS IN CORRECT TYPE
    if( not isinstance(window_size_x, np.uint32) ):
        print("vglClConvolution: Warning: window_size_x not np.uint32! Trying to convert...")
        try:
            window_size_x = np.uint32(window_size_x)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert window_size_x as a np.uint32 object.")
            print(str(e))
            exit()
    # EVALUATING IF window_size_y IS IN CORRECT TYPE
    if( not isinstance(window_size_y, np.uint32) ):
        print("vglClConvolution: Warning: window_size_y not np.uint32! Trying to convert...")
        try:
            window_size_y = np.uint32(window_size_y)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert window_size_y as a np.uint32 object.")
            print(str(e))
            exit()
    # EVALUATING IF window_size_z IS IN CORRECT TYPE
    if( not isinstance(window_size_z, np.uint32) ):
        print("vglClConvolution: Warning: window_size_z not np.uint32! Trying to convert...")
        try:
            window_size_z = np.uint32(window_size_z)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert window_size_z as a np.uint32 object.")
            print(str(e))
            exit()

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglCl3dErode.cl", "vglCl3dErode")
    _kernel = _program.vglCl3dErode

    _kernel.set_arg(0, img_input.get_oclPtr())
    _kernel.set_arg(1, img_output.get_oclPtr())
    _kernel.set_arg(2, mobj_convolution_window)
    _kernel.set_arg(3, window_size_x)
    _kernel.set_arg(4, window_size_y)
    _kernel.set_arg(5, window_size_z)

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input.get_oclPtr().shape, None)

    mobj_convolution_window = None
    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Direct copy from src to dst.

  */    
"""
def vglCl3dMax(img_input1, img_input2, img_output):

    vl.vglCheckContext(img_input1, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_input2, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglCl3dMax.cl", "vglCl3dMax")
    _kernel = _program.vglCl3dMax

    _kernel.set_arg(0, img_input1.get_oclPtr())
    _kernel.set_arg(1, img_input2.get_oclPtr())
    _kernel.set_arg(2, img_output.get_oclPtr())

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input1.get_oclPtr().shape, None)

    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Direct copy from src to dst.

  */    
"""
def vglCl3dMin(img_input1, img_input2, img_output):

    vl.vglCheckContext(img_input1, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_input2, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglCl3dMin.cl", "vglCl3dMin")
    _kernel = _program.vglCl3dMin

    _kernel.set_arg(0, img_input1.get_oclPtr())
    _kernel.set_arg(1, img_input2.get_oclPtr())
    _kernel.set_arg(2, img_output.get_oclPtr())

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input1.get_oclPtr().shape, None)

    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Direct copy from src to dst.

  */    
"""
def vglCl3dNot(img_input, img_output):

    vl.vglCheckContext(img_input, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglCl3dNot.cl", "vglCl3dNot")
    _kernel = _program.vglCl3dNot

    _kernel.set_arg(0, img_input.get_oclPtr())
    _kernel.set_arg(1, img_output.get_oclPtr())

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input.get_oclPtr().shape, None)

    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Direct copy from src to dst.

  */    
"""
def vglCl3dSub(img_input1, img_input2, img_output):

    vl.vglCheckContext(img_input1, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_input2, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglCl3dSub.cl", "vglCl3dSub")
    _kernel = _program.vglCl3dSub

    _kernel.set_arg(0, img_input1.get_oclPtr())
    _kernel.set_arg(1, img_input2.get_oclPtr())
    _kernel.set_arg(2, img_output.get_oclPtr())

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input1.get_oclPtr().shape, None)

    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Direct copy from src to dst.

  */    
"""
def vglCl3dSum(img_input1, img_input2, img_output):

    vl.vglCheckContext(img_input1, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_input2, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglCl3dSum.cl", "vglCl3dSum")
    _kernel = _program.vglCl3dSum

    _kernel.set_arg(0, img_input1.get_oclPtr())
    _kernel.set_arg(1, img_input2.get_oclPtr())
    _kernel.set_arg(2, img_output.get_oclPtr())

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input1.get_oclPtr().shape, None)

    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Threshold of src image by float parameter. if the pixel is below thresh,
    the output is 0, else, the output is top. Result is stored in dst image.
  */    
"""
def vglCl3dThreshold(src, dst, thresh, top = 1.0):

    vl.vglCheckContext(src, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(dst, vl.VGL_CL_CONTEXT())
    # EVALUATING IF thresh IS IN CORRECT TYPE
    if( not isinstance(thresh, np.float32) ):
        print("vglClConvolution: Warning: thresh not np.float32! Trying to convert...")
        try:
            thresh = np.float32(thresh)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert thresh as a np.float32 object.")
            print(str(e))
            exit()
    # EVALUATING IF top IS IN CORRECT TYPE
    if( not isinstance(top, np.float32) ):
        print("vglClConvolution: Warning: top not np.float32! Trying to convert...")
        try:
            top = np.float32(top)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert top as a np.float32 object.")
            print(str(e))
            exit()

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglCl3dThreshold.cl", "vglCl3dThreshold")
    _kernel = _program.vglCl3dThreshold

    _kernel.set_arg(0, src.get_oclPtr())
    _kernel.set_arg(1, dst.get_oclPtr())
    _kernel.set_arg(2, thresh)
    _kernel.set_arg(3, top)

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, src.get_oclPtr().shape, None)

    vl.vglSetContext(dst, vl.VGL_CL_CONTEXT())

"""
    /** Convolution of src image by mask. Result is stored in dst image.

  */    
"""
def vglClBlurSq3(img_input, img_output):

    vl.vglCheckContext(img_input, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglClBlurSq3.cl", "vglClBlurSq3")
    _kernel = _program.vglClBlurSq3

    _kernel.set_arg(0, img_input.get_oclPtr())
    _kernel.set_arg(1, img_output.get_oclPtr())

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input.get_oclPtr().shape, None)

    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Convolution of src image by mask. Result is stored in dst image.

  */    
"""
def vglClConvolution(img_input, img_output, convolution_window, window_size_x, window_size_y):

    vl.vglCheckContext(img_input, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())
    # EVALUATING IF convolution_window IS IN CORRECT TYPE
    try:
        mobj_convolution_window = cl.Buffer(vl.get_ocl().context, cl.mem_flags.READ_ONLY, convolution_window.nbytes)
        cl.enqueue_copy(vl.get_ocl().commandQueue, mobj_convolution_window, convolution_window.tobytes(), is_blocking=True)
        convolution_window = mobj_convolution_window
    except Exception as e:
        print("vglClConvolution: Error!! Impossible to convert convolution_window to cl.Buffer object.")
        print(str(e))
        exit()
    # EVALUATING IF window_size_x IS IN CORRECT TYPE
    if( not isinstance(window_size_x, np.uint32) ):
        print("vglClConvolution: Warning: window_size_x not np.uint32! Trying to convert...")
        try:
            window_size_x = np.uint32(window_size_x)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert window_size_x as a np.uint32 object.")
            print(str(e))
            exit()
    # EVALUATING IF window_size_y IS IN CORRECT TYPE
    if( not isinstance(window_size_y, np.uint32) ):
        print("vglClConvolution: Warning: window_size_y not np.uint32! Trying to convert...")
        try:
            window_size_y = np.uint32(window_size_y)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert window_size_y as a np.uint32 object.")
            print(str(e))
            exit()

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglClConvolution.cl", "vglClConvolution")
    _kernel = _program.vglClConvolution

    _kernel.set_arg(0, img_input.get_oclPtr())
    _kernel.set_arg(1, img_output.get_oclPtr())
    _kernel.set_arg(2, mobj_convolution_window)
    _kernel.set_arg(3, window_size_x)
    _kernel.set_arg(4, window_size_y)

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input.get_oclPtr().shape, None)

    mobj_convolution_window = None
    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Direct copy from src to dst.

  */    
"""
def vglClCopy(img_input, img_output):

    vl.vglCheckContext(img_input, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglClCopy.cl", "vglClCopy")
    _kernel = _program.vglClCopy

    _kernel.set_arg(0, img_input.get_oclPtr())
    _kernel.set_arg(1, img_output.get_oclPtr())

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input.get_oclPtr().shape, None)

    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Erosion of src image by mask. Result is stored in dst image.

  */    
"""
def vglClDilate(img_input, img_output, convolution_window, window_size_x, window_size_y):

    vl.vglCheckContext(img_input, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())
    # EVALUATING IF convolution_window IS IN CORRECT TYPE
    try:
        mobj_convolution_window = cl.Buffer(vl.get_ocl().context, cl.mem_flags.READ_ONLY, convolution_window.nbytes)
        cl.enqueue_copy(vl.get_ocl().commandQueue, mobj_convolution_window, convolution_window.tobytes(), is_blocking=True)
        convolution_window = mobj_convolution_window
    except Exception as e:
        print("vglClConvolution: Error!! Impossible to convert convolution_window to cl.Buffer object.")
        print(str(e))
        exit()
    # EVALUATING IF window_size_x IS IN CORRECT TYPE
    if( not isinstance(window_size_x, np.uint32) ):
        print("vglClConvolution: Warning: window_size_x not np.uint32! Trying to convert...")
        try:
            window_size_x = np.uint32(window_size_x)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert window_size_x as a np.uint32 object.")
            print(str(e))
            exit()
    # EVALUATING IF window_size_y IS IN CORRECT TYPE
    if( not isinstance(window_size_y, np.uint32) ):
        print("vglClConvolution: Warning: window_size_y not np.uint32! Trying to convert...")
        try:
            window_size_y = np.uint32(window_size_y)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert window_size_y as a np.uint32 object.")
            print(str(e))
            exit()

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglClDilate.cl", "vglClDilate")
    _kernel = _program.vglClDilate

    _kernel.set_arg(0, img_input.get_oclPtr())
    _kernel.set_arg(1, img_output.get_oclPtr())
    _kernel.set_arg(2, mobj_convolution_window)
    _kernel.set_arg(3, window_size_x)
    _kernel.set_arg(4, window_size_y)

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input.get_oclPtr().shape, None)

    mobj_convolution_window = None
    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Erosion of src image by mask. Result is stored in dst image.

  */    
"""
def vglClErode(img_input, img_output, convolution_window, window_size_x, window_size_y):

    vl.vglCheckContext(img_input, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())
    # EVALUATING IF convolution_window IS IN CORRECT TYPE
    try:
        mobj_convolution_window = cl.Buffer(vl.get_ocl().context, cl.mem_flags.READ_ONLY, convolution_window.nbytes)
        cl.enqueue_copy(vl.get_ocl().commandQueue, mobj_convolution_window, convolution_window.tobytes(), is_blocking=True)
        convolution_window = mobj_convolution_window
    except Exception as e:
        print("vglClConvolution: Error!! Impossible to convert convolution_window to cl.Buffer object.")
        print(str(e))
        exit()
    # EVALUATING IF window_size_x IS IN CORRECT TYPE
    if( not isinstance(window_size_x, np.uint32) ):
        print("vglClConvolution: Warning: window_size_x not np.uint32! Trying to convert...")
        try:
            window_size_x = np.uint32(window_size_x)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert window_size_x as a np.uint32 object.")
            print(str(e))
            exit()
    # EVALUATING IF window_size_y IS IN CORRECT TYPE
    if( not isinstance(window_size_y, np.uint32) ):
        print("vglClConvolution: Warning: window_size_y not np.uint32! Trying to convert...")
        try:
            window_size_y = np.uint32(window_size_y)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert window_size_y as a np.uint32 object.")
            print(str(e))
            exit()

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglClErode.cl", "vglClErode")
    _kernel = _program.vglClErode

    _kernel.set_arg(0, img_input.get_oclPtr())
    _kernel.set_arg(1, img_output.get_oclPtr())
    _kernel.set_arg(2, mobj_convolution_window)
    _kernel.set_arg(3, window_size_x)
    _kernel.set_arg(4, window_size_y)

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input.get_oclPtr().shape, None)

    mobj_convolution_window = None
    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Negative of src image. Result is stored in dst image.

  */    
"""
def vglClInvert(img_input, img_output):

    vl.vglCheckContext(img_input, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglClInvert.cl", "vglClInvert")
    _kernel = _program.vglClInvert

    _kernel.set_arg(0, img_input.get_oclPtr())
    _kernel.set_arg(1, img_output.get_oclPtr())

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input.get_oclPtr().shape, None)

    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Direct copy from src to dst.

  */    
"""
def vglClMax(img_input1, img_input2, img_output):

    vl.vglCheckContext(img_input1, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_input2, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglClMax.cl", "vglClMax")
    _kernel = _program.vglClMax

    _kernel.set_arg(0, img_input1.get_oclPtr())
    _kernel.set_arg(1, img_input2.get_oclPtr())
    _kernel.set_arg(2, img_output.get_oclPtr())

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input1.get_oclPtr().shape, None)

    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Direct copy from src to dst.

  */    
"""
def vglClMin(img_input1, img_input2, img_output):

    vl.vglCheckContext(img_input1, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_input2, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglClMin.cl", "vglClMin")
    _kernel = _program.vglClMin

    _kernel.set_arg(0, img_input1.get_oclPtr())
    _kernel.set_arg(1, img_input2.get_oclPtr())
    _kernel.set_arg(2, img_output.get_oclPtr())

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input1.get_oclPtr().shape, None)

    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Direct copy from src to dst.

  */    
"""
def vglClSub(img_input1, img_input2, img_output):

    vl.vglCheckContext(img_input1, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_input2, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglClSub.cl", "vglClSub")
    _kernel = _program.vglClSub

    _kernel.set_arg(0, img_input1.get_oclPtr())
    _kernel.set_arg(1, img_input2.get_oclPtr())
    _kernel.set_arg(2, img_output.get_oclPtr())

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input1.get_oclPtr().shape, None)

    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Direct copy from src to dst.

  */    
"""
def vglClSum(img_input1, img_input2, img_output):

    vl.vglCheckContext(img_input1, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_input2, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(img_output, vl.VGL_CL_CONTEXT())

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglClSum.cl", "vglClSum")
    _kernel = _program.vglClSum

    _kernel.set_arg(0, img_input1.get_oclPtr())
    _kernel.set_arg(1, img_input2.get_oclPtr())
    _kernel.set_arg(2, img_output.get_oclPtr())

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, img_input1.get_oclPtr().shape, None)

    vl.vglSetContext(img_output, vl.VGL_CL_CONTEXT())

"""
    /** Swap R and B channels.
  */    
"""
def vglClSwapRgb(src, dst):

    vl.vglCheckContext(src, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(dst, vl.VGL_CL_CONTEXT())

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglClSwapRgb.cl", "vglClSwapRgb")
    _kernel = _program.vglClSwapRgb

    _kernel.set_arg(0, src.get_oclPtr())
    _kernel.set_arg(1, dst.get_oclPtr())

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, src.get_oclPtr().shape, None)

    vl.vglSetContext(dst, vl.VGL_CL_CONTEXT())

"""
    /** Threshold of src image by float parameter. if the pixel is below thresh,
    the output is 0, else, the output is top. Result is stored in dst image.
  */    
"""
def vglClThreshold(src, dst, thresh, top = 1.0):

    vl.vglCheckContext(src, vl.VGL_CL_CONTEXT())
    vl.vglCheckContext(dst, vl.VGL_CL_CONTEXT())
    # EVALUATING IF thresh IS IN CORRECT TYPE
    if( not isinstance(thresh, np.float32) ):
        print("vglClConvolution: Warning: thresh not np.float32! Trying to convert...")
        try:
            thresh = np.float32(thresh)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert thresh as a np.float32 object.")
            print(str(e))
            exit()
    # EVALUATING IF top IS IN CORRECT TYPE
    if( not isinstance(top, np.float32) ):
        print("vglClConvolution: Warning: top not np.float32! Trying to convert...")
        try:
            top = np.float32(top)
        except Exception as e:
            print("vglClConvolution: Error!! Impossible to convert top as a np.float32 object.")
            print(str(e))
            exit()

    _program = vl.get_ocl_context().get_compiled_kernel("CL/vglClThreshold.cl", "vglClThreshold")
    _kernel = _program.vglClThreshold

    _kernel.set_arg(0, src.get_oclPtr())
    _kernel.set_arg(1, dst.get_oclPtr())
    _kernel.set_arg(2, thresh)
    _kernel.set_arg(3, top)

    # THIS IS A BLOCKING COMMAND. IT EXECUTES THE KERNEL.
    cl.enqueue_nd_range_kernel(vl.get_ocl().commandQueue, _kernel, src.get_oclPtr().shape, None)

    vl.vglSetContext(dst, vl.VGL_CL_CONTEXT())

