### Instruction

- Place the simulator (Deccq_V2.0.1.1) in the root directory.
- Place the license plate dataset in the root directory
- Adjust the absolute path to the scenario json file in the `start.bat` file
- run the bat file
- install pyhton dependencies (see `requirements.txt`) and run `detector.py`

### Issues

- It seems that the simulator doesn't use the correct coordination for the viewpoint (loading from the json file) and moves the view point down. As an example, if you place a viewpoint to close to the ground, the simulator takes picture from under the ground!
- Interval between photo capturing
- Total number of image, not the number of image per viewpoint
- absolute path to the scenario json is needed

### Funding 
This work is done by [Infotiv AB](https://www.infotiv.se) under [VALU3S](https://valu3s.eu) project in a collaboration with [RISE](https://www.ri.se) under [ITEA3](https://itea4.org) European [IVVES](https://itea4.org/project/ivves.html) project. This project has received funding from the [ECSEL](https://www.ecsel.eu) Joint Undertaking (JU) under grant agreement No 876852. The JU receives support from the European Union’s Horizon 2020 research and innovation programme and Austria, Czech Republic, Germany, Ireland, Italy, Portugal, Spain, Sweden, Turkey.

The ECSEL JU and the European Commission are not responsible for the content on this website or any use that may be made of the information it contains.


INFOTIV AB | RISE Research Institutes of Sweden | CAMEA  | VALU3S Project
------------ |  ------------  | ------------ | ------------ 
![](resources/logos/INFOTIV-logo.png)  | ![](resources/logos/RISE-logo.png)  | ![](resources/logos/camea-logo.png) |  ![](resources/logos/VALU3S-logo.png) 

This project is started and is currently maintained by [Hamid Ebadi](https://github.com/ebadi).

