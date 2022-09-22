
### Cut a 531s video to a 518s video with new start and end times
|       | CPU (s) | GPU (s) |
|:------|:-------:|:-------:|
| cut 1 |   371   |    -    |
| cut 2 |   377   |    -    |
| cut 3 |   374   |    -    |

### Merge the cut videos 
|       | CPU (s) | GPU (s) |
|:------|:-------:|:-------:|
| merge |   407   |    -    |


### Compression of a 4GB video file
|                          | CPU (s) | GPU (s) | Data size (GB) |
|:-------------------------|:-------:|:-------:|:--------------:|
| h.264 preset ultrafast   |   382   |    -    |      4.04      |
| h.264 preset veryfast    |   481   |    -    |      1.27      |
| h.264 preset medium      |  1213   |    -    |      1.87      |
| h.264 preset slower      |  2651   |    -    |      1.81      |
| h.265 preset ultrafast   |  2567   |    -    |     0.620      |
| h.265 preset medium      |  8318   |    -    |      1.32      |

### Extracting 1064 images
|                  | CPU (s) | GPU (s) |
|:-----------------|:-------:|:-------:|
| image extraction |   374   |    -    |

### Extracting and object detection for 1064 images 

|                  | CPU (s) | GPU (s) |
|:-----------------|:-------:|:-------:|
| image extraction & object detection|   602   |    -    |


