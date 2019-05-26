=====
Usage
=====

To run fzf_template, use the provided command:
    
    fzf_template

If you installed using pipsi, the entrypoint script will be added to your path.

Options can be discovered using the `-h` script option. 

Config can be passed using the `-i` option and should match the following format:

.. code-block:: yaml

    values: 
      "identifier 1":
        key1: value1
        key2: value2
      "identifier 2":
        key3: value3
        key4: value4
    templates:
      - src: ~/.config/fzf_template/templates/template1.conf
        dest: ~/.app/conf1.conf
      - src: template2.conf
        dest: ~/.app/conf2.conf
