<?xml version="1.0" encoding="UTF-8"?>
<model ref="r:ce3fdcc2-fcb9-4695-8179-76805c3ce7f6(beauty.shop.structure)">
  <persistence version="9" />
  <languages>
    <devkit ref="78434eb8-b0e5-444b-850d-e7c4ad2da9ab(jetbrains.mps.devkit.aspect.structure)" />
  </languages>
  <imports>
    <import index="tpck" ref="r:00000000-0000-4000-0000-011c89590288(jetbrains.mps.lang.core.structure)" implicit="true" />
  </imports>
  <registry>
    <language id="c72da2b9-7cce-4447-8389-f407dc1158b7" name="jetbrains.mps.lang.structure">
      <concept id="1169125787135" name="jetbrains.mps.lang.structure.structure.AbstractConceptDeclaration" flags="ig" index="PkWjJ">
        <property id="6714410169261853888" name="conceptId" index="EcuMT" />
        <child id="1071489727083" name="linkDeclaration" index="1TKVEi" />
        <child id="1071489727084" name="propertyDeclaration" index="1TKVEl" />
      </concept>
      <concept id="1071489090640" name="jetbrains.mps.lang.structure.structure.ConceptDeclaration" flags="ig" index="1TIwiD">
        <reference id="1071489389519" name="extends" index="1TJDcQ" />
      </concept>
      <concept id="1071489288299" name="jetbrains.mps.lang.structure.structure.PropertyDeclaration" flags="ig" index="1TJgyi">
        <property id="241647608299431129" name="propertyId" index="IQ2nx" />
        <reference id="1082985295845" name="dataType" index="AX2Wp" />
      </concept>
      <concept id="1071489288298" name="jetbrains.mps.lang.structure.structure.LinkDeclaration" flags="ig" index="1TJgyj">
        <property id="1071599776563" name="role" index="20kJfa" />
        <property id="1071599893252" name="sourceCardinality" index="20lbJX" />
        <property id="241647608299431140" name="linkId" index="IQ2ns" />
        <reference id="1071599976176" name="target" index="20lvS9" />
      </concept>
    </language>
    <language id="ceab5195-25ea-4f22-9b92-103b95ca8c0c" name="jetbrains.mps.lang.core">
      <concept id="1169194658468" name="jetbrains.mps.lang.core.structure.INamedConcept" flags="ng" index="TrEIO">
        <property id="1169194664001" name="name" index="TrG5h" />
      </concept>
    </language>
  </registry>
  <node concept="1TIwiD" id="5ItmJMm6UlL">
    <property role="EcuMT" value="6601532669691667825" />
    <property role="TrG5h" value="BeautyShop" />
    <ref role="1TJDcQ" to="tpck:gw2VY9q" />
    <node concept="1TJgyi" id="5ItmJMm6VQT" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674041" />
      <property role="TrG5h" value="location" />
      <ref role="AX2Wp" to="tpck:fKAOsGN" resolve="string" />
    </node>
    <node concept="1TJgyi" id="5ItmJMm6VQV" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674043" />
      <property role="TrG5h" value="square" />
      <ref role="AX2Wp" to="tpck:fKAQMTA" resolve="integer" />
    </node>
    <node concept="1TJgyj" id="5ItmJMm6VQY" role="1TKVEi">
      <property role="IQ2ns" value="6601532669691674046" />
      <property role="20kJfa" value="selesmam" />
      <property role="20lbJX" value="fLJekj4/_1" />
      <ref role="20lvS9" node="5ItmJMm6VQR" resolve="Salesman" />
    </node>
    <node concept="1TJgyj" id="5ItmJMm6VR$" role="1TKVEi">
      <property role="IQ2ns" value="6601532669691674084" />
      <property role="20kJfa" value="assiatant" />
      <property role="20lbJX" value="fLJekj4/_1" />
      <ref role="20lvS9" node="5ItmJMm6VRz" resolve="Assistant" />
    </node>
    <node concept="1TJgyj" id="5ItmJMm6VRZ" role="1TKVEi">
      <property role="IQ2ns" value="6601532669691674111" />
      <property role="20kJfa" value="makeup" />
      <ref role="20lvS9" node="5ItmJMm6VS3" resolve="Makeup" />
    </node>
    <node concept="1TJgyj" id="5ItmJMm6VSd" role="1TKVEi">
      <property role="IQ2ns" value="6601532669691674125" />
      <property role="20kJfa" value="perfume" />
      <ref role="20lvS9" node="5ItmJMm6VSD" resolve="Perfume" />
    </node>
    <node concept="1TJgyj" id="5ItmJMm6VSi" role="1TKVEi">
      <property role="IQ2ns" value="6601532669691674130" />
      <property role="20kJfa" value="hair" />
      <ref role="20lvS9" node="5ItmJMm6VSJ" resolve="Hair" />
    </node>
  </node>
  <node concept="1TIwiD" id="5ItmJMm6VQR">
    <property role="EcuMT" value="6601532669691674039" />
    <property role="TrG5h" value="Salesman" />
    <ref role="1TJDcQ" to="tpck:gw2VY9q" />
    <node concept="1TJgyi" id="5ItmJMm6VR7" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674055" />
      <property role="TrG5h" value="name" />
      <ref role="AX2Wp" to="tpck:fKAOsGN" resolve="string" />
    </node>
    <node concept="1TJgyi" id="5ItmJMm6VRi" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674066" />
      <property role="TrG5h" value="age" />
      <ref role="AX2Wp" to="tpck:fKAQMTA" resolve="integer" />
    </node>
    <node concept="1TJgyi" id="5ItmJMm6VRm" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674070" />
      <property role="TrG5h" value="salary" />
      <ref role="AX2Wp" to="tpck:fKAQMTA" resolve="integer" />
    </node>
    <node concept="1TJgyi" id="5ItmJMm6VRu" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674078" />
      <property role="TrG5h" value="workingtime" />
      <ref role="AX2Wp" to="tpck:fKAQMTA" resolve="integer" />
    </node>
  </node>
  <node concept="1TIwiD" id="5ItmJMm6VRz">
    <property role="EcuMT" value="6601532669691674083" />
    <property role="TrG5h" value="Assistant" />
    <ref role="1TJDcQ" to="tpck:gw2VY9q" />
    <node concept="1TJgyi" id="5ItmJMm6VRB" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674087" />
      <property role="TrG5h" value="name" />
      <ref role="AX2Wp" to="tpck:fKAOsGN" resolve="string" />
    </node>
    <node concept="1TJgyi" id="5ItmJMm6VRG" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674092" />
      <property role="TrG5h" value="age" />
      <ref role="AX2Wp" to="tpck:fKAQMTA" resolve="integer" />
    </node>
    <node concept="1TJgyi" id="5ItmJMm6VRK" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674096" />
      <property role="TrG5h" value="salary" />
      <ref role="AX2Wp" to="tpck:fKAQMTA" resolve="integer" />
    </node>
    <node concept="1TJgyi" id="5ItmJMm6VRP" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674101" />
      <property role="TrG5h" value="workingtime" />
      <ref role="AX2Wp" to="tpck:fKAQMTA" resolve="integer" />
    </node>
  </node>
  <node concept="1TIwiD" id="5ItmJMm6VS3">
    <property role="EcuMT" value="6601532669691674115" />
    <property role="TrG5h" value="Makeup" />
    <ref role="1TJDcQ" to="tpck:gw2VY9q" />
    <node concept="1TJgyi" id="5ItmJMm6VS$" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674148" />
      <property role="TrG5h" value="square" />
      <ref role="AX2Wp" to="tpck:fKAQMTA" resolve="integer" />
    </node>
    <node concept="1TJgyi" id="5ItmJMm6VSA" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674150" />
      <property role="TrG5h" value="sections" />
      <ref role="AX2Wp" to="tpck:fKAQMTA" resolve="integer" />
    </node>
  </node>
  <node concept="1TIwiD" id="5ItmJMm6VSD">
    <property role="EcuMT" value="6601532669691674153" />
    <property role="TrG5h" value="Perfume" />
    <ref role="1TJDcQ" to="tpck:gw2VY9q" />
    <node concept="1TJgyi" id="5ItmJMm6VSE" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674154" />
      <property role="TrG5h" value="square" />
      <ref role="AX2Wp" to="tpck:fKAQMTA" resolve="integer" />
    </node>
    <node concept="1TJgyi" id="5ItmJMm6VSG" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674156" />
      <property role="TrG5h" value="sections" />
      <ref role="AX2Wp" to="tpck:fKAQMTA" resolve="integer" />
    </node>
  </node>
  <node concept="1TIwiD" id="5ItmJMm6VSJ">
    <property role="EcuMT" value="6601532669691674159" />
    <property role="TrG5h" value="Hair" />
    <ref role="1TJDcQ" to="tpck:gw2VY9q" />
    <node concept="1TJgyi" id="5ItmJMm6VSK" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674160" />
      <property role="TrG5h" value="sections" />
      <ref role="AX2Wp" to="tpck:fKAQMTA" resolve="integer" />
    </node>
    <node concept="1TJgyi" id="5ItmJMm6VSQ" role="1TKVEl">
      <property role="IQ2nx" value="6601532669691674166" />
      <property role="TrG5h" value="square" />
      <ref role="AX2Wp" to="tpck:fKAQMTA" resolve="integer" />
    </node>
  </node>
</model>

