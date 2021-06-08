<template>
  <div>
    <GChart 
			:settings="{ packages: ['corechart', 'gauge'] }"
			type="Gauge"
		 	:data="data" 
			:options="options" />
  </div>
</template>

<script>
export default {
  name: "GraphCard",
  props: ["data", "options"],
};
</script>