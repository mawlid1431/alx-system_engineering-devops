# 1-install_a_package.pp

# Ensure the package is installed with pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
