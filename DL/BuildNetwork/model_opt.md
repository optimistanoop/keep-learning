## Build the Neural Network
### The function model_opt is implemented correctly.

* Awesome !! AdamOptimizer is recommended optimizer which was also used in DC GAN arch project developed by facebook, additionally you have made sure that all updates are computed before running optimizer by use of `control_dependencies`.

* In order to improve your networks faces generation please wrap your g_train_opt with
with `tf.control_dependencies(tf.get_collection(tf.GraphKeys.UPDATE_OPS, scope='generator'))` because `tf.control_dependencies()` is required in creation of the batch normalization layers.

* Good !! AdamOptimizer is recommended optimizer which was also used in DC GAN arch project developed by facebook, additionally you have made sure that all updates are computed before running optimizer by use of `control_dependencies`.

* To improve performance of networks and to generate realistic faces please wrap your `g_train_opt`
with `tf.control_dependencies(tf.get_collection(tf.GraphKeys.UPDATE_OPS, scope='generator'))` because `tf.control_dependencies()` makes sure that all updates are computed before running optimizer.