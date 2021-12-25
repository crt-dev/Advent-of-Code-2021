import unittest
from ..d16 import *

class d16tests(unittest.TestCase):
    def test_D2FE28_create_packet(self):
        input = "D2FE28"
        pf = PacketFactory.create_from_hex(input)
        packet = pf.create_packet()
        self.assertEqual(packet.version, 6)
        self.assertEqual(packet.type, 4)
        self.assertEqual(packet.literal, 2021)
        pf.mq.assert_empty()

    def test_D2FE28_create_packets(self):
        input = "D2FE28"
        pf = PacketFactory.create_from_hex(input)
        packets = pf.create_packets()
        self.assertEqual(len(packets), 1)
        packet = packets[0]
        self.assertEqual(packet.version, 6)
        self.assertEqual(packet.type, 4)
        self.assertEqual(packet.literal, 2021)
        pf.mq.assert_empty()

    def test_D2FE28_create_packets_2(self):
        input = "D2FE28D2FE28"
        pf = PacketFactory.create_from_hex(input)
        packets = pf.create_packets()
        self.assertEqual(len(packets), 2)
        for p in packets:
            self.assertEqual(p.version, 6)
            self.assertEqual(p.type, 4)
            self.assertEqual(p.literal, 2021)
        pf.mq.assert_empty()

    def evaluate_38006F45291200(self, input, check_empty):
        pf = PacketFactory.create_from_hex(input)
        packet = pf.create_packet()
        self.assertEqual(packet.version, 1)
        self.assertEqual(packet.type, 6)
        self.assertEqual(packet.length_type, 0)
        self.assertEqual(packet.sp_length, 27)
        self.assertEqual(len(packet.sub_packets), 2)

        sp1 = packet.sub_packets[0]
        sp2 = packet.sub_packets[1]

        self.assertEqual(sp1.literal, 10)
        self.assertEqual(sp2.literal, 20)

        if check_empty:
            pf.mq.assert_empty()


    def test_38006F45291200_minus_a_zero(self):
        input = "38006F4529120"
        self.evaluate_38006F45291200(input, True) #trailing zero doesn't encode anything and breaks my sanity check on queue size

    def test_38006F45291200(self):
        input = "38006F45291200"
        self.evaluate_38006F45291200(input, False)

    def test_EE00D40C823060(self):
        input = "EE00D40C823060"
        pf = PacketFactory.create_from_hex(input)
        packet = pf.create_packet()

        self.assertEqual(packet.version, 7)
        self.assertEqual(packet.type, 3)

        sp1 = packet.sub_packets[0]
        sp2 = packet.sub_packets[1]
        sp3 = packet.sub_packets[2]
        self.assertEqual(sp1.literal, 1)
        self.assertEqual(sp2.literal, 2)
        self.assertEqual(sp3.literal, 3)

        #pf.mq.assert_empty()

    def test_8A004A801A8002F478(self):
        """
        8A004A801A8002F478 represents an operator packet (version 4)
        which contains an operator packet (version 1)
        which contains an operator packet (version 5)
        which contains a literal value (version 6);
        this packet has a version sum of 16.
        """

        input = "8A004A801A8002F478"
        pf = PacketFactory.create_from_hex(input)
        packet = pf.create_packet()

        self.assertEqual(packet.version, 4)
        sp1 = packet.sub_packets[0]
        self.assertEqual(sp1.version, 1)
        sp2 = sp1.sub_packets[0]
        self.assertEqual(sp2.version, 5)
        sp3 = sp2.sub_packets[0]
        self.assertEqual(sp3.version, 6)
        self.assertTrue(sp3.literal is not None)

        version_sum = sum_version([packet])
        self.assertEqual(version_sum, 16)

    def test_620080001611562C8802118E34(self):
        """
        620080001611562C8802118E34 represents an operator packet (version 3)
        which contains two sub-packets;
            each sub-packet is an operator packet that contains two literal values.
        This packet has a version sum of 12.
        """

        input = "620080001611562C8802118E34"
        pf = PacketFactory.create_from_hex(input)
        packet = pf.create_packet()

        self.assertEqual(packet.version, 3)
        self.assertEqual(len(packet.sub_packets), 2)
        sp1 = packet.sub_packets[0]
        sp2 = packet.sub_packets[1]
        self.assertEqual(len(sp1.sub_packets), 2)
        self.assertEqual(len(sp2.sub_packets), 2)

        sps = [sp1.sub_packets[0], sp1.sub_packets[1], sp2.sub_packets[0], sp2.sub_packets[1]]
        self.assertTrue(sp.literal is not None for sp in sps)

        version_sum = sum_version([packet])
        self.assertEqual(version_sum, 12)

    def test_C0015000016115A2E0802F182340(self):
        """
        C0015000016115A2E0802F182340 has the same structure as the previous example,
        but the outermost packet uses a different length type ID.
        This packet has a version sum of 23.
        :return:
        """
        input = "C0015000016115A2E0802F182340"
        pf = PacketFactory.create_from_hex(input)
        packet = pf.create_packet()

        self.assertEqual(len(packet.sub_packets), 2)
        sp1 = packet.sub_packets[0]
        sp2 = packet.sub_packets[1]
        self.assertEqual(len(sp1.sub_packets), 2)
        self.assertEqual(len(sp2.sub_packets), 2)
        sps = [sp1.sub_packets[0], sp1.sub_packets[1], sp2.sub_packets[0], sp2.sub_packets[1]]
        self.assertTrue(sp.literal is not None for sp in sps)

        version_sum = sum_version([packet])
        self.assertEqual(version_sum, 23)

    def test_A0016C880162017C3686B18A3D4780(self):
        """
        A0016C880162017C3686B18A3D4780 is an operator packet
            that contains an operator packet
                that contains an operator packet
                    that contains five literal values;
        it has a version sum of 31.
        :return:
        """

        input = "A0016C880162017C3686B18A3D4780"
        pf = PacketFactory.create_from_hex(input)
        packet = pf.create_packet()
        sp1 = packet.sub_packets[0]
        sp2 = sp1.sub_packets[0]

        self.assertEqual(len(sp2.sub_packets), 5)
        self.assertTrue(sp.literal is not None for sp in sp2.sub_packets)

        version_sum = sum_version([packet])
        self.assertEqual(version_sum, 31)

    """
C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
04005AC33890 finds the product of 6 and 9, resulting in the value 54.
880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
D8005AC2A8F0 produces 1, because 5 is less than 15.
F600BC2D8F produces 0, because 5 is not greater than 15.
9C005AC2F8F0 produces 0, because 5 is not equal to 15.
9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.
"""

    def test_C200B40A82_sum(self):
        input = "C200B40A82"
        value = get_value(input)
        self.assertEqual(value, 3)