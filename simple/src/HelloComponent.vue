<template>
    <h1 class="t">Hellocomponent {{ msg }}</h1>
</template>

<script>
export default {
    name:"HellComponent",
    data(){
        return{
            msg:"欢迎"
        }
    },
}
</script>

<style>

.t{
    color: red;

}
</style>
