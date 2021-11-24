using System;
using Xunit;
using VMWareSet;

namespace VMWareSetTests
{
    public class UnitTest1
    {

        public UnitTest1()
        {
            Set s = new Set();
        }

        [Fact]
        public void isEmptyTest()
        {

            Assert.Equal(true, s.isEmpty());
        }

        [Fact]
        public void getSizeTest()
        {
            
            Assert.Equal(0, s.getSize());
        }

        
        [Fact]
        public void addTest()
        {
            s.Add(1);
            Assert.Equal(s.getSize(), 1);
        }
    }
}
